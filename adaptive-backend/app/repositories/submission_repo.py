from sqlalchemy.orm import Session
from app.models.submission import Submission

def create_submission(db: Session, data: dict):
    submission = Submission(**data)
    db.add(submission)
    db.commit()
    db.refresh(submission)
    return submission