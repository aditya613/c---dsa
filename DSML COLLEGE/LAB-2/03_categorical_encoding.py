# Lab 2 - Part 3: Categorical Encoding (One-Hot & Label Encoding)
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

path = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_raw.csv")
df = pd.read_csv(path)

# 1. Fill missing categorical values with Mode (most frequent)
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

# 2. One-Hot Encoding (drop_first=True avoids Dummy Variable Trap)
dummies = pd.get_dummies(df["Department"], prefix="Dept", drop_first=True)
print("One-Hot Encoded (Dummy Variables):")
print(dummies.head())

# 3. Label Encoding (Converts categories into numbers 0, 1, 2...)
le = LabelEncoder()
df["Education_Code"] = le.fit_transform(df["Education_Level"].fillna("Unknown"))
print("\nLabel Encoded Education Level:")
print(df[["Education_Level", "Education_Code"]].head())
