from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.submission import Submission
from app.models.problem import Problem
from app.schemas.submission import SubmissionCreate
from app.services.execution_service import execute_code
from app.services.skill_service import update_skills_for_submission
from app.services import ml_service
from typing import Dict, Any, List


def create_submission(db: Session, submission_data: SubmissionCreate) -> Dict[str, Any]:
    # Fetch problem (must exist or return a clean 404 to the client)
    problem: Problem | None = (
        db.query(Problem)
        .filter(Problem.id == submission_data.problem_id)
        .one_or_none()
    )
    if problem is None:
        # Return an API-friendly error instead of a server error
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )

    # Execute code (no DB writes in execution layer)
    exec_result = execute_code(db=db, problem_id=problem.id, code=submission_data.code, language=submission_data.language)

    status = exec_result.get("status")
    score = float(exec_result.get("score", 0.0))
    execution_time_ms = int(exec_result.get("execution_time_ms", 0) or 0)

    passed = status == "passed"

    # Update skills atomically and compute deltas
    skill_delta_map, mastery_delta, updated_super_band = update_skills_for_submission(db, submission_data.user_id, problem, passed)

    # Save immutable submission snapshot
    new_sub = Submission(
        user_id=submission_data.user_id,
        problem_id=problem.id,
        code=submission_data.code,
        language=submission_data.language,
        status=status,
        score=score,
        execution_time_ms=execution_time_ms,
        difficulty_band=problem.difficulty_band,
        super_band=problem.super_band,
        cluster=problem.cluster,
        skill_delta=skill_delta_map,
        mastery_delta=mastery_delta,
    )

    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)

    # Trigger ML microservice (non-blocking)
    try:
        payload = {
            "user_id": submission_data.user_id,
            "problem_id": problem.id,
            "score": score,
            "cluster": problem.cluster,
            "difficulty_band": problem.difficulty_band,
            "skills": problem.skills_tested,
        }
        ml_service.trigger_ml_event(payload)
    except Exception:
        pass

    # Adaptive response
    resp = {
        "submission_id": new_sub.id,
        "status": status,
        "score": score,
        "execution_time_ms": execution_time_ms,
        "mastery_delta": mastery_delta,
        "updated_super_band": updated_super_band,
    }

    return resp


def get_user_submissions(db: Session, user_id: int) -> List[Submission]:
    return db.query(Submission).filter(Submission.user_id == user_id).order_by(Submission.created_at.desc()).all()