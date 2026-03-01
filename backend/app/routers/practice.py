"""Practice routes for coding problems."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.practice import ProblemResponse, CodeSubmissionRequest, SubmissionResultSchema
from app.core.database import get_db

router = APIRouter(prefix="/api/practice", tags=["practice"])


@router.get("/problems", response_model=List[ProblemResponse])
def get_problems(
    difficulty: str = None,
    topic: str = None,
    db: Session = Depends(get_db)
):
    """Get available problems with optional filtering."""
    # TODO: Implement get problems logic
    pass


@router.get("/problems/{problem_id}", response_model=ProblemResponse)
def get_problem(problem_id: int, db: Session = Depends(get_db)):
    """Get a specific problem by ID."""
    # TODO: Implement get problem logic
    pass


@router.post("/submit", response_model=SubmissionResultSchema)
def submit_code(
    submission: CodeSubmissionRequest,
    db: Session = Depends(get_db)
):
    """Submit code for execution and testing."""
    # TODO: Implement code submission logic
    pass


@router.get("/submissions/{user_id}", response_model=List[SubmissionResultSchema])
def get_user_submissions(user_id: int, db: Session = Depends(get_db)):
    """Get all submissions for a user."""
    # TODO: Implement get submissions logic
    pass
