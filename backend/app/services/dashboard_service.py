"""Dashboard service for analytics and user statistics."""

from sqlalchemy.orm import Session
from typing import Dict, List
from app.models.user import User
from app.models.skill_state import SkillState
from app.models.submission import Submission
from datetime import datetime


class DashboardService:
    @staticmethod
    def get_user_performance_stats(db: Session, user_id: int) -> Dict:
        total_submissions = db.query(Submission).filter(Submission.user_id == user_id).count()
        total_passed = db.query(Submission).filter(Submission.user_id == user_id, Submission.status == "passed").count()
        total_solved = total_passed
        avg_exec = db.query(Submission.execution_time_ms).filter(Submission.user_id == user_id).all()
        avg_time = 0.0
        if avg_exec:
            times = [t[0] or 0 for t in avg_exec]
            avg_time = float(sum(times) / len(times)) if times else 0.0

        acceptance_rate = float(total_passed) / float(total_submissions) if total_submissions > 0 else 0.0

        return {
            "total_problems_solved": total_solved,
            "total_submissions": total_submissions,
            "acceptance_rate": acceptance_rate,
            "average_execution_time": avg_time,
            "total_study_time": 0,  # placeholder - requires tracking study sessions
        }

    @staticmethod
    def get_user_skill_states(db: Session, user_id: int) -> List[SkillState]:
        return db.query(SkillState).filter(SkillState.user_id == user_id).all()

    @staticmethod
    def calculate_mastery_level(db: Session, user_id: int, skill_name: str) -> float:
        state = db.query(SkillState).filter(SkillState.user_id == user_id, SkillState.skill_name == skill_name).one_or_none()
        return float(state.current_mastery) if state is not None else 0.0

    @staticmethod
    def get_topic_breakdown(db: Session, user_id: int) -> Dict:
        rows = db.query(Submission.cluster, Submission.status).filter(Submission.user_id == user_id).all()
        breakdown: Dict[str, Dict[str, int]] = {}
        for cluster, status in rows:
            if cluster not in breakdown:
                breakdown[cluster] = {"passed": 0, "failed": 0, "runtime_error": 0}
            breakdown[cluster][status] = breakdown[cluster].get(status, 0) + 1
        return breakdown

    @staticmethod
    def get_recent_submissions(db: Session, user_id: int, limit: int = 10) -> List[Submission]:
        return db.query(Submission).filter(Submission.user_id == user_id).order_by(Submission.created_at.desc()).limit(limit).all()

