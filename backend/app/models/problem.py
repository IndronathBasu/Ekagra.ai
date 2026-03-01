from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.dialects.postgresql import JSONB
from app.core.database import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)

    domain = Column(String(100), nullable=False)
    subject = Column(String(100), nullable=False)
    topic = Column(String(100), nullable=False)
    cluster = Column(String(150), nullable=False)

    question_type = Column(String(50), nullable=False)
    cognitive_dimension = Column(String(100), nullable=False)

    difficulty_band = Column(Integer, nullable=False)
    super_band = Column(Integer, nullable=False)

    concepts = Column(JSONB, nullable=False)         # List
    skills_tested = Column(JSONB, nullable=False)   # List

    problem_statement = Column(Text, nullable=False)
    example_input = Column(Text, nullable=True)
    example_output = Column(Text, nullable=True)

    estimated_time_seconds = Column(Integer, nullable=False)
    mastery_weight = Column(Float, nullable=False)

    metadata_ = Column("metadata", JSONB, nullable=True)