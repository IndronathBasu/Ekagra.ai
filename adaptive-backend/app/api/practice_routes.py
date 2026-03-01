from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.submission_schema import SubmissionCreate
from app.services.practice_service import process_submission_and_get_next

router = APIRouter()

@router.post("/submit")
def submit_answer(payload: SubmissionCreate, db: Session = Depends(get_db)):
    return process_submission_and_get_next(db, payload.dict())