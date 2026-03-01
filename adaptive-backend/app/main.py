from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.models  # ← THIS LINE IS CRITICAL

from app.api.practice_routes import router as practice_router

# --------------------------------------------------
# Create FastAPI App Instance
# --------------------------------------------------

app = FastAPI(
    title="Skill Engine Backend",
    description="Adaptive Learning Engine API",
    version="1.0.0"
)

# --------------------------------------------------
# CORS Configuration (Required for React Frontend)
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Health Check Endpoint
# --------------------------------------------------

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}

# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/", tags=["System"])
def root():
    return {
        "message": "Skill Engine Backend is running",
        "docs": "/docs"
    }

# --------------------------------------------------
# Register Routers
# --------------------------------------------------

app.include_router(
    practice_router,
    prefix="/practice",
    tags=["Practice"]
)

# --------------------------------------------------
# Startup Event (Optional Logging)
# --------------------------------------------------

@app.on_event("startup")
def startup_event():
    print("🚀 Skill Engine Backend Started Successfully")