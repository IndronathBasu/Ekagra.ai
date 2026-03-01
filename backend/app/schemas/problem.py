from pydantic import BaseModel
from typing import List, Optional, Dict


class ProblemBase(BaseModel):
    domain: str
    subject: str
    topic: str
    cluster: str

    question_type: str
    cognitive_dimension: str

    difficulty_band: int
    super_band: int

    concepts: List[str]
    skills_tested: List[str]

    problem_statement: str
    example_input: Optional[str]
    example_output: Optional[str]

    estimated_time_seconds: int
    mastery_weight: float

    metadata_: Optional[Dict]


class ProblemCreate(ProblemBase):
    pass


class ProblemResponse(ProblemBase):
    id: int

    class Config:
        from_attributes = True