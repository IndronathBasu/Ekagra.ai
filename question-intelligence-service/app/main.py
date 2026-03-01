from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Question Intelligence Service")

app.include_router(router, prefix="/api/v1")