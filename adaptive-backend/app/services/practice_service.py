from sqlalchemy.orm import Session
from app.repositories.submission_repo import create_submission
from app.services.skill_service import update_skill_state
from app.models.problem import Problem
from app.models.skill_state import SkillState


def get_next_problem(db: Session, user_id: int):
    """
    Simple adaptive logic:
    - Get user's weakest topic
    - Return a problem from that topic
    """

    skill = (
        db.query(SkillState)
        .filter(SkillState.user_id == user_id)
        .order_by(SkillState.mastery_score.asc())
        .first()
    )

    if not skill:
        # If no skill data, return any problem
        return db.query(Problem).first()

    return (
        db.query(Problem)
        .filter(Problem.topic == skill.topic)
        .first()
    )


def process_submission_and_get_next(db: Session, submission_data: dict):

    # 1. Save submission
    submission = create_submission(db, submission_data)

    # 2. Get problem
    problem = db.query(Problem).filter(
        Problem.id == submission.problem_id
    ).first()

    if not problem:
        raise Exception("Problem not found")

    # 3. Update skill
    update_skill_state(
        db,
        submission.user_id,
        problem.topic,
        submission.is_correct
    )

    # 4. Return next adaptive problem
    return get_next_problem(db, submission.user_id)