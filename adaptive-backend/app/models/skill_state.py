from sqlalchemy import Column, Integer, Float, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base

class SkillState(Base):
    __tablename__ = "skill_states"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    topic = Column(String(100), nullable=False)
    mastery_score = Column(Float, default=0.0)
    total_attempts = Column(Integer, default=0)
    total_correct = Column(Integer, default=0)
    last_practiced = Column(TIMESTAMP, server_default=func.now())