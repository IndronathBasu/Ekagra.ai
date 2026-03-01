from app.models.predictor import DifficultyPredictor

predictor = DifficultyPredictor()

def predict(request):
    return predictor.predict(request)