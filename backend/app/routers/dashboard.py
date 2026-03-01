"""Dashboard routes for analytics and performance tracking."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.dashboard import DashboardResponse, SkillStateResponse, PerformanceStatsResponse, RecentSubmissionResponse
from app.core.database import get_db
from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/stats/{user_id}", response_model=DashboardResponse)
def get_dashboard_stats(user_id: int, db: Session = Depends(get_db)):
    perf = DashboardService.get_user_performance_stats(db, user_id)
    skills = DashboardService.get_user_skill_states(db, user_id)
    recent = DashboardService.get_recent_submissions(db, user_id)

    skill_states = [
        {
            "topic": s.skill_name,
            "mastery_level": s.current_mastery,
            "problems_solved": s.total_success,
            "problems_attempted": s.total_attempts,
            "last_updated": s.last_updated,
        }
        for s in skills
    ]

    recent_subs = [
        {
            "id": r.id,
            "problem_title": r.cluster,
            "status": r.status,
            "language": r.language,
            "created_at": r.created_at,
        }
        for r in recent
    ]

    response = {
        "user_id": user_id,
        "skill_states": skill_states,
        "performance_stats": perf,
        "recent_submissions": recent_subs,
    }

    return response


@router.get("/skills/{user_id}", response_model=list[SkillStateResponse])
def get_user_skills(user_id: int, db: Session = Depends(get_db)):
    skills = DashboardService.get_user_skill_states(db, user_id)
    return [
        {
            "topic": s.skill_name,
            "mastery_level": s.current_mastery,
            "problems_solved": s.total_success,
            "problems_attempted": s.total_attempts,
            "last_updated": s.last_updated,
        }
        for s in skills
    ]


@router.get("/performance/{user_id}", response_model=PerformanceStatsResponse)
def get_performance_stats(user_id: int, db: Session = Depends(get_db)):
    return DashboardService.get_user_performance_stats(db, user_id)


@router.get("/chart-data/{user_id}")
def get_chart_data(user_id: int, db: Session = Depends(get_db)):
    # Provide simple mastery heatmap data
    skills = DashboardService.get_user_skill_states(db, user_id)
    return {s.skill_name: s.current_mastery for s in skills}
