import os
from dotenv import load_dotenv

# Load environment variables from .env (development convenience)
load_dotenv()

# Core security and app configuration. Values default to safe dev values
# but should be overridden in production via environment variables.

SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# Development helper: set to 'true' to bypass authentication checks
# Use only in local development environments.
DISABLE_AUTH = os.getenv("DISABLE_AUTH", "false").lower() in ("1", "true", "yes")

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
