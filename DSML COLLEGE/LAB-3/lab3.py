# ============================================================
# LAB 3: Feature Scaling (StandardScaler vs. MinMaxScaler)
# Dataset Used: Medical Insurance Dataset (insurance_kaggle.csv)
# ============================================================
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 1. Load Dataset
data_path = os.path.join(os.path.dirname(__file__), "dataset", "insurance_kaggle.csv")
if not os.path.exists(data_path):
    data_path = "dataset/insurance_kaggle.csv"
df = pd.read_csv(data_path)

print(f"1. Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
features = df[["age", "bmi", "charges"]]

# 2. Original Statistics Before Scaling
print("\n2. Summary Statistics BEFORE Scaling:")
print(features.describe().loc[["mean", "std", "min", "max"]])

# 3. Standardization / Z-score Normalization
# Formula: Z = (X - mean) / std  -> Results in mean=0, std=1
scaler_std = StandardScaler()
features_std = scaler_std.fit_transform(features)
df_std = pd.DataFrame(features_std, columns=features.columns)

print("\n3. Summary Statistics AFTER Standard Scaling (Z-Score):")
print(df_std.describe().loc[["mean", "std", "min", "max"]].round(2))

# 4. Min-Max Normalization
# Formula: X_norm = (X - min) / (max - min) -> Bounded strictly to [0, 1]
scaler_minmax = MinMaxScaler()
features_minmax = scaler_minmax.fit_transform(features)
df_minmax = pd.DataFrame(features_minmax, columns=features.columns)

print("\n4. Summary Statistics AFTER Min-Max Scaling [0, 1]:")
print(df_minmax.describe().loc[["min", "max"]].round(2))

print("\n[+] Feature Scaling Analysis Completed Successfully!")
