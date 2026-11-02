# LAB 2: Data Preprocessing and Imputation Pipeline (Titanic Dataset)
import os
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# 1. Load Dataset
path = os.path.join(os.path.dirname(__file__), "dataset", "titanic_kaggle.csv")
df = pd.read_csv(path)
print(f"Loaded Titanic Dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# 2. Check Missing Values
print("\nMissing values before imputation:")
print(df[["Age", "Embarked"]].isnull().sum())

# 3. Impute Numerical Column (Age -> Median)
age_imputer = SimpleImputer(strategy="median")
df["Age"] = age_imputer.fit_transform(df[["Age"]])

# 4. Impute Categorical Column (Embarked -> Mode)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\nMissing values after imputation:")
print(df[["Age", "Embarked"]].isnull().sum())

# 5. Categorical Encoding (One-Hot Encoding with drop_first=True)
df_encoded = pd.get_dummies(df[["Sex", "Embarked"]], drop_first=True)

# 6. Feature Scaling on Numerical Features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[["Age", "Fare"]])

print("\nPreprocessed Features:")
print("- Encoded Categories Shape:", df_encoded.shape)
print("- Scaled Numerical Shape:   ", scaled_features.shape)
print("\nPreprocessing Completed Successfully!")
