from pydantic import BaseModel

class QuestionRequest(BaseModel):
    problem_statement: str
    concepts: str
    skills_tested: str
    cognitive_dimension: str
    estimated_time_seconds: int