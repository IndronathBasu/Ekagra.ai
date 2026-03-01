import torch
from app.models.model_loader import ModelLoader

class DifficultyPredictor:

    def __init__(self):
        loader = ModelLoader()
        self.tokenizer = loader.tokenizer
        self.model = loader.model

    def predict(self, request):

        text = f"""
        Problem: {request.problem_statement}
        Concepts: {request.concepts}
        Skills: {request.skills_tested}
        Cognitive Level: {request.cognitive_dimension}
        Estimated Time: {request.estimated_time_seconds}
        """

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        probs = torch.softmax(outputs.logits, dim=1)
        band = torch.argmax(probs).item() + 1
        confidence = probs.max().item()

        super_band = (band - 1) // 3 + 1

        return {
            "difficulty_band": band,
            "super_band": super_band,
            "confidence": confidence
        }