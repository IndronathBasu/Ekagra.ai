"""Practice schemas for problems and submissions."""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TestCaseSchema(BaseModel):
    id: int
    input_data: str
    expected_output: str
    is_hidden: int
    
    class Config:
        from_attributes = True


class ProblemResponse(BaseModel):
    id: int
    title: str
    description: str
    difficulty: str
    topic: str
    test_cases: List[TestCaseSchema] = []
    
    class Config:
        from_attributes = True


class CodeSubmissionRequest(BaseModel):
    problem_id: int
    code: str
    language: str


class SubmissionResultSchema(BaseModel):
    id: int
    status: str
    execution_time: float
    memory_used: float
    created_at: datetime
    
    class Config:
        from_attributes = True
