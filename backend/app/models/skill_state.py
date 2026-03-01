from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from datetime import datetime
from app.core.database import Base


class SkillState(Base):
    __tablename__ = "user_skill_state"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_name = Column(String(150), nullable=False)
    current_mastery = Column(Float, default=0.0)
    super_band = Column(Integer, default=0)
    total_attempts = Column(Integer, default=0)
    total_success = Column(Integer, default=0)
    last_updated = Column(DateTime, default=datetime.utcnow, server_default=func.now())


# composite index for fast lookup by user and skill name
Index('ix_user_skill_state_user_skill', SkillState.user_id, SkillState.skill_name)
