import torch
from torch.utils.data import Dataset

class DifficultyDataset(Dataset):

    def __init__(self, dataframe, tokenizer, max_len=512):
        self.df = dataframe.reset_index(drop=True)
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):

        row = self.df.iloc[idx]

        text = f"""
        Problem: {row.problem_statement}
        Concepts: {row.concepts}
        Skills: {row.skills_tested}
        Cognitive Level: {row.cognitive_dimension}
        Estimated Time: {row.estimated_time_seconds}
        """

        encoding = self.tokenizer(
            text,
            truncation=True,
            padding="max_length",
            max_length=self.max_len,
            return_tensors="pt"
        )

        return {
            "input_ids": encoding["input_ids"].squeeze(),
            "attention_mask": encoding["attention_mask"].squeeze(),
            "labels": int(row.difficulty_band) - 1
        }