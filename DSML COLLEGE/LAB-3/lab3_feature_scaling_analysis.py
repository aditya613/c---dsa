# LAB 3: Feature Scaling Analysis (Insurance Dataset)
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 1. Load Dataset
path = os.path.join(os.path.dirname(__file__), "dataset", "insurance_kaggle.csv")
df = pd.read_csv(path)
print("Insurance Dataset Loaded. Shape:", df.shape)

features = df[["age", "bmi", "charges"]]

# 2. Before Scaling
print("\n--- Original Summary Statistics ---")
print(features.describe().loc[["mean", "std", "min", "max"]])

# 3. Apply Standard Scaling (Z-score)
scaler_std = StandardScaler()
features_std = scaler_std.fit_transform(features)
df_std = pd.DataFrame(features_std, columns=features.columns)

print("\n--- After Standard Scaling (Mean ~ 0, Std ~ 1) ---")
print(df_std.describe().loc[["mean", "std", "min", "max"]].round(2))

# 4. Apply Min-Max Scaling [0, 1]
scaler_minmax = MinMaxScaler()
features_minmax = scaler_minmax.fit_transform(features)
df_minmax = pd.DataFrame(features_minmax, columns=features.columns)

print("\n--- After Min-Max Scaling (Min = 0, Max = 1) ---")
print(df_minmax.describe().loc[["min", "max"]].round(2))
