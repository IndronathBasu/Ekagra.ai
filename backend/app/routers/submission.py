from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.submission import SubmissionCreate, SubmissionResponse, FullSubmissionRecord
from app.services.submission_service import (
    create_submission,
    get_user_submissions,
)

router = APIRouter(prefix="/submissions", tags=["Submissions"])


@router.post("", response_model=SubmissionResponse)
@router.post("/", response_model=SubmissionResponse)  # Support both with and without trailing slash
def submit_code(submission: SubmissionCreate, db: Session = Depends(get_db)):
    return create_submission(db, submission)


@router.get("/user/{user_id}", response_model=List[FullSubmissionRecord])
def fetch_user_submissions(user_id: int, db: Session = Depends(get_db)):
    return get_user_submissions(db, user_id)