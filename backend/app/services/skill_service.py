from __future__ import annotations

from typing import Dict, List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.skill_state import SkillState
from app.models.problem import Problem
from datetime import datetime


def compute_mastery_delta(passed: bool, mastery_weight: float) -> float:
    if passed:
        return float(mastery_weight)
    return - float(mastery_weight) * 0.2


def _increase_super_band_if_needed(state: SkillState) -> bool:
    # Simple threshold: every 1.0 mastery increases super_band by 1
    try:
        threshold = (state.super_band + 1) * 1.0
        if state.current_mastery >= threshold:
            state.super_band = state.super_band + 1
            return True
    except Exception:
        pass
    return False


def update_skills_for_submission(db: Session, user_id: int, problem: Problem, passed: bool) -> Tuple[Dict[str, float], float, int]:
    """Update skill states for all skills tested by `problem`.

    Returns: (skill_delta_map, mastery_delta_total, updated_super_band)
    """
    mastery_delta = compute_mastery_delta(passed, problem.mastery_weight)
    skill_deltas: Dict[str, float] = {}
    updated_super_band = 0

    skills = problem.skills_tested or []

    with db.begin():
        for skill in skills:
            # find existing state
            state = db.query(SkillState).filter(SkillState.user_id == user_id, SkillState.skill_name == skill).one_or_none()
            if state is None:
                state = SkillState(user_id=user_id, skill_name=skill, current_mastery=0.0, super_band=0, total_attempts=0, total_success=0)
                db.add(state)
                db.flush()

            state.total_attempts = (state.total_attempts or 0) + 1
            if passed:
                state.total_success = (state.total_success or 0) + 1

            state.current_mastery = float((state.current_mastery or 0.0) + mastery_delta)
            state.last_updated = datetime.utcnow()

            crossed = _increase_super_band_if_needed(state)
            if crossed:
                updated_super_band = state.super_band

            skill_deltas[skill] = mastery_delta

    return skill_deltas, mastery_delta, updated_super_band
