from pydantic import BaseModel
from typing import Optional, List, Dict


class SubmissionCreate(BaseModel):
    problem_id: int
    user_id: int   # temporary until auth restored
    code: str
    language: str


class SubmissionResponse(BaseModel):
    submission_id: int
    status: str
    score: float
    execution_time_ms: Optional[int]
    mastery_delta: float
    updated_super_band: int

    class Config:
        from_attributes = True


class FullSubmissionRecord(BaseModel):
    id: int
    user_id: int
    problem_id: int
    code: str
    language: str
    status: str
    score: float
    execution_time_ms: Optional[int]
    difficulty_band: int
    super_band: int
    cluster: str
    skill_delta: Optional[Dict[str, float]]
    mastery_delta: Optional[float]
    created_at: Optional[str]

    class Config:
        from_attributes = True