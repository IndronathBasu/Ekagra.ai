from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.problem import ProblemCreate, ProblemResponse
from app.services.problem_service import (
    create_problem,
    get_problem_by_id,
    get_all_problems,
)

router = APIRouter(prefix="/problems", tags=["Problems"])


# Create Problem (Admin)
@router.post("", response_model=ProblemResponse)
def create_new_problem(problem: ProblemCreate, db: Session = Depends(get_db)):
    return create_problem(db, problem)


# Get All Problems (supports both /problems and /problems/)
@router.get("/", response_model=List[ProblemResponse])
@router.get("", response_model=List[ProblemResponse])
def fetch_problems(
    skip: int = 0,
    limit: int = 10,
    difficulty_band: int | None = None,
    topic: str | None = None,
    db: Session = Depends(get_db),
):
    return get_all_problems(db, skip, limit, difficulty_band, topic)


# Get Single Problem
@router.get("/{problem_id}", response_model=ProblemResponse)
def fetch_problem(problem_id: int, db: Session = Depends(get_db)):
    problem = get_problem_by_id(db, problem_id)

    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    return problem