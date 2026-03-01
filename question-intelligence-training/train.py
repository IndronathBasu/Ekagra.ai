import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments
)
from dataset import DifficultyDataset
import config

def main():

    df = pd.read_csv(config.DATA_PATH)

    df["difficulty_band"] = df["difficulty_band"].astype(int)

    train_df, val_df = train_test_split(
        df,
        test_size=0.15,
        stratify=df["difficulty_band"],
        random_state=42
    )

    tokenizer = AutoTokenizer.from_pretrained(config.MODEL_NAME)

    train_dataset = DifficultyDataset(train_df, tokenizer, config.MAX_LENGTH)
    val_dataset = DifficultyDataset(val_df, tokenizer, config.MAX_LENGTH)

    model = AutoModelForSequenceClassification.from_pretrained(
        config.MODEL_NAME,
        num_labels=config.NUM_LABELS
    )

    training_args = TrainingArguments(
        output_dir=config.OUTPUT_DIR,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=config.LEARNING_RATE,
        per_device_train_batch_size=config.BATCH_SIZE,
        per_device_eval_batch_size=config.BATCH_SIZE,
        num_train_epochs=config.EPOCHS,
        weight_decay=0.01,
        load_best_model_at_end=True,
        logging_dir="./logs"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )

    trainer.train()

    trainer.save_model(config.OUTPUT_DIR)
    tokenizer.save_pretrained(config.OUTPUT_DIR)

    print("Training Complete")

if __name__ == "__main__":
    main()