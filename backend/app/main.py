from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

# Import models so SQLAlchemy registers them
from app.models import user, problem, test_case, submission, skill_state

# Routers
from app.routers import auth, problem, submission, dashboard

#test
from sqlalchemy import text
from app.core.database import engine


app = FastAPI()

# -----------------------------
# Create tables in database
# -----------------------------
#Base.metadata.create_all(bind=engine)

# -----------------------------
# CORS (for frontend later)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    # during development the front end may be accessed via localhost or
    # 127.0.0.1; mismatched origin strings will trigger CORS failures which
    # manifest as "Network Error" in the browser.  a permissive policy
    # avoids confusion.  In production this should be locked down to the
    # actual deployed origin(s).
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Include Routers (all under /api)
# -----------------------------
app.include_router(auth.router, prefix="/api")
app.include_router(problem.router, prefix="/api")
app.include_router(submission.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")

# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def health():
    return {"status": "Backend running"}

@app.post("/health-test")
def health_test():
    return {"status": "ok"}



@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"db": "connected"}