from sqlalchemy.orm import Session
from app.models.skill_state import SkillState
from datetime import datetime

def update_skill_state(db: Session, user_id: int, topic: str, is_correct: bool):

    skill = (
        db.query(SkillState)
        .filter(SkillState.user_id == user_id, SkillState.topic == topic)
        .first()
    )

    if not skill:
        skill = SkillState(
            user_id=user_id,
            topic=topic,
            mastery_score=0.0,
            total_attempts=0,
            total_correct=0
        )
        db.add(skill)

    skill.total_attempts += 1

    if is_correct:
        skill.total_correct += 1

    skill.mastery_score = skill.total_correct / skill.total_attempts
    skill.last_practiced = datetime.utcnow()

    db.commit()