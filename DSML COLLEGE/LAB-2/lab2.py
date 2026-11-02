# ============================================================
# LAB 2: Data Preprocessing, Imputation & Encoding
# Dataset Used: Titanic Dataset (titanic_kaggle.csv)
# ============================================================
import os
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# 1. Load Dataset
data_path = os.path.join(os.path.dirname(__file__), "dataset", "titanic_kaggle.csv")
if not os.path.exists(data_path):
    data_path = "dataset/titanic_kaggle.csv"
df = pd.read_csv(data_path)

print(f"1. Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst 3 rows:\n", df[["PassengerId", "Age", "Sex", "Embarked", "Fare"]].head(3))

# 2. Check Missing Data
print("\n2. Missing values count before imputation:")
print(df[["Age", "Embarked"]].isnull().sum())

# 3. Numerical Imputation (Age -> Median)
# Median is used because it is robust against outliers
imputer_num = SimpleImputer(strategy="median")
df["Age"] = imputer_num.fit_transform(df[["Age"]])

# 4. Categorical Imputation (Embarked -> Mode / Most Frequent)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\nMissing values count after imputation:")
print(df[["Age", "Embarked"]].isnull().sum())

# 5. Categorical Encoding (One-Hot Encoding with drop_first=True)
# drop_first=True resolves the Dummy Variable Trap (multicollinearity)
df_encoded = pd.get_dummies(df[["Sex", "Embarked"]], drop_first=True)
print("\n3. Encoded Categorical Features (First 3 rows):")
print(df_encoded.head(3))

# 6. Feature Scaling (StandardScaler: mean=0, std=1)
scaler = StandardScaler()
scaled_numerical = scaler.fit_transform(df[["Age", "Fare"]])
print("\n4. Scaled Numerical Features (First 3 rows):\n", scaled_numerical[:3])

print("\n[+] Data Preprocessing Pipeline Completed Successfully!")
