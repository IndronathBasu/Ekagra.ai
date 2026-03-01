from transformers import AutoTokenizer, AutoModelForSequenceClassification

class ModelLoader:

    def __init__(self, model_path="trained_model"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.model.eval()