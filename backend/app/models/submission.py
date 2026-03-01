from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from app.core.database import Base


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    problem_id = Column(Integer, ForeignKey("problems.id", ondelete="CASCADE"), nullable=False, index=True)

    code = Column(Text, nullable=False)
    language = Column(String(50), nullable=False)

    status = Column(String(50), nullable=False)  # passed / failed / runtime_error
    score = Column(Float, nullable=False)

    execution_time_ms = Column(Integer, nullable=True)

    # Adaptive tracking fields
    difficulty_band = Column(Integer, nullable=False)
    super_band = Column(Integer, nullable=False)
    cluster = Column(String(150), nullable=False)

    skill_delta = Column(JSONB, nullable=True)   # {"logic_building": +0.1}
    mastery_delta = Column(Float, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


# add indexes for fast filtering
Index('ix_submissions_user_problem', Submission.user_id, Submission.problem_id)
