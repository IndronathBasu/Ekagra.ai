from pydantic import BaseModel

class PredictionResponse(BaseModel):
    difficulty_band: int
    super_band: int
    confidence: float