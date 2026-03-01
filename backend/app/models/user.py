from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from app.core.database import Base


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	email = Column(String(255), unique=True, index=True, nullable=False)
	hashed_password = Column(String(255), nullable=False)
	name = Column(String(255), nullable=False)
	role = Column(String(50), default="user", nullable=False)
	created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())
