# Lab 2 - Part 4: End-to-End Preprocessing with ColumnTransformer
import os
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

path = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_raw.csv")
df = pd.read_csv(path)

# Separate feature subsets
num_features = ["Experience_Years", "Salary"]
cat_features = ["Department", "Remote_Work"]

# Pipeline for numbers: Median Impute + Standard Scale
num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Pipeline for categories: Mode Impute + One-Hot Encode
cat_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(drop="first", sparse_output=False))
])

# Combine into ColumnTransformer
preprocessor = ColumnTransformer([
    ("num", num_pipe, num_features),
    ("cat", cat_pipe, cat_features)
])

# Fit and transform
X_clean = preprocessor.fit_transform(df)
print("Clean Processed Feature Matrix Shape:", X_clean.shape)
print("First row of clean data:\n", X_clean[0])
