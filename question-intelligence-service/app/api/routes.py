from fastapi import APIRouter
from app.schemas.request_schema import QuestionRequest
from app.schemas.response_schema import PredictionResponse
from app.services.inference_service import predict

router = APIRouter()

@router.post("/predict-difficulty", response_model=PredictionResponse)
def predict_route(request: QuestionRequest):
    return predict(request)