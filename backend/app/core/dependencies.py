from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_token, hash_password
from app.models.user import User
from app.core.config import DISABLE_AUTH

# If DISABLE_AUTH is set, return or create a local dev user so protected
# endpoints continue to work without valid JWTs. This is intended only for
# development; keep authentication enabled in production.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=not DISABLE_AUTH)


def _create_dev_user(db: Session):
    """
    Create or return a dev user for prototype mode.
    This allows all endpoints to work without authentication.
    """
    dev_email = "dev@example.com"
    user = db.query(User).filter(User.email == dev_email).first()
    if user:
        return user

    # Create dev user if it doesn't exist
    hashed_pw = hash_password("devpass")
    new_user = User(email=dev_email, hashed_password=hashed_pw, name="Dev User", role="admin")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Get current user. In prototype mode (DISABLE_AUTH=true), 
    automatically creates/returns a dev user without requiring a token.
    """
    # Prototype bypass - no auth required
    if DISABLE_AUTH:
        return _create_dev_user(db)

    # Production mode - require valid JWT token
    payload = decode_token(token)
    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user
