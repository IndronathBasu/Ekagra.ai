from sqlalchemy.orm import Session
from typing import List
from app.models.problem import Problem
from app.schemas.problem import ProblemCreate


def create_problem(db: Session, problem_data: ProblemCreate) -> Problem:
    new_problem = Problem(**problem_data.dict())
    db.add(new_problem)
    db.commit()
    db.refresh(new_problem)
    return new_problem


def get_problem_by_id(db: Session, problem_id: int) -> Problem | None:
    return db.query(Problem).filter(Problem.id == problem_id).first()


def get_all_problems(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    difficulty_band: int | None = None,
    topic: str | None = None,
):
    query = db.query(Problem)

    if difficulty_band is not None:
        query = query.filter(Problem.difficulty_band == difficulty_band)

    if topic is not None:
        query = query.filter(Problem.topic == topic)

    return query.offset(skip).limit(limit).all()