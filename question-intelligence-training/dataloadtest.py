import pandas as pd

df = pd.read_csv(r"E:\ml_engine\dataset\final_adaptive_dataset.csv")

print(df.shape)
print(df.columns)
print(df["difficulty_band"].value_counts())