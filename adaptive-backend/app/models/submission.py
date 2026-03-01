from sqlalchemy import Column, Integer, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    problem_id = Column(Integer, ForeignKey("problems.id", ondelete="CASCADE"))
    is_correct = Column(Boolean, nullable=False)
    time_taken = Column(Integer)
    attempt_number = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, server_default=func.now())