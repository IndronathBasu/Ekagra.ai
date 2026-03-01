from sqlalchemy.orm import Session
from app.models.problem import Problem

def get_problem_by_topic_and_band(db: Session, topic: str, min_band: int, max_band: int):
    return (
        db.query(Problem)
        .filter(
            Problem.topic == topic,
            Problem.difficulty_band >= min_band,
            Problem.difficulty_band <= max_band
        )
        .order_by(Problem.id)
        .first()
    )