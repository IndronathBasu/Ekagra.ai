from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base

class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(100), nullable=False)
    topic = Column(String(100), nullable=False, index=True)
    difficulty_band = Column(Integer, nullable=False, index=True)
    super_band = Column(Integer, nullable=False)
    problem_statement = Column(Text, nullable=False)
    estimated_time_seconds = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())