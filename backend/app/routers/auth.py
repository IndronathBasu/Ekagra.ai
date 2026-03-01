from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import RegisterRequest, LoginRequest, AuthResponse
from app.services.auth_service import register_user, login_user
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=AuthResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(db, data.email, data.password, data.name)


@router.post("/login", response_model=AuthResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, data.email, data.password)