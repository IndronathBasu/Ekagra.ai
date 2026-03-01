from pydantic import BaseModel

class SubmissionCreate(BaseModel):
    user_id: int
    problem_id: int
    is_correct: bool
    time_taken: int