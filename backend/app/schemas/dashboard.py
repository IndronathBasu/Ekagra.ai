"""Dashboard schemas for analytics and statistics."""

from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime


class SkillStateResponse(BaseModel):
    topic: str
    mastery_level: float
    problems_solved: int
    problems_attempted: int
    last_updated: datetime
    
    class Config:
        from_attributes = True


class PerformanceStatsResponse(BaseModel):
    total_problems_solved: int
    total_submissions: int
    acceptance_rate: float
    average_execution_time: float
    total_study_time: int  # in minutes


class RecentSubmissionResponse(BaseModel):
    id: int
    problem_title: str
    status: str
    language: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class DashboardResponse(BaseModel):
    user_id: int
    skill_states: List[SkillStateResponse]
    performance_stats: PerformanceStatsResponse
    recent_submissions: List[RecentSubmissionResponse]
