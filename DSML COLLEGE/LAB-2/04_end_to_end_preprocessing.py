"""
LAB 2 - Step 4: Complete End-to-End Preprocessing Pipeline
Topics Covered:
1. Building modular preprocessing pipelines using Scikit-Learn.
2. Numerical pipeline: Median imputation + Standard scaling.
3. Categorical pipeline: Mode imputation + One-hot encoding (drop='first').
4. Combining pipelines using ColumnTransformer.
5. Transforming raw, messy tabular data into a ML-ready feature matrix X and target y.
"""

import os
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

print("=" * 80)
print("LAB 2 - PART 4: UNIFIED DATA PREPROCESSING PIPELINE")
print("=" * 80)

dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_raw.csv")
df = pd.read_csv(dataset_path)

print(f"Raw Input Dataset Shape: {df.shape}")
print(df.head(5))

# Separate target variable (Performance_Rating) from feature set
target_col = "Performance_Rating"

# Handle target missing values by dropping or imputing mode
df = df.dropna(subset=[target_col]).reset_index(drop=True)

X = df.drop(columns=["EmployeeID", "Name", target_col])
y_raw = df[target_col]

# Define feature subsets
numerical_features = ["Experience_Years", "Salary"]
categorical_features = ["Department", "Education_Level", "Remote_Work"]

print(f"\nTarget Variable: '{target_col}' ({len(y_raw)} samples)")
print(f"Numerical Features: {numerical_features}")
print(f"Categorical Features: {categorical_features}")

# Build Modular Sub-Pipelines
num_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(drop='first', sparse_output=False))
])

# Combine via ColumnTransformer
preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, numerical_features),
    ('cat', cat_pipeline, categorical_features)
])

# Fit and Transform Features
X_processed = preprocessor.fit_transform(X)

# Retrieve transformed column names
cat_encoder_step = preprocessor.named_transformers_['cat'].named_steps['encoder']
cat_encoded_cols = list(cat_encoder_step.get_feature_names_out(categorical_features))
all_processed_cols = numerical_features + cat_encoded_cols

# Encode target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y_raw)

# Construct final clean DataFrame
df_clean = pd.DataFrame(X_processed, columns=all_processed_cols)
df_clean["Target_Performance"] = y_encoded

print("\n" + "=" * 50)
print("FINAL PREPROCESSED DATASET (Ready for ML Modeling)")
print("=" * 50)
print(f"Processed Shape: {df_clean.shape} (All NaNs resolved, all categoricals encoded)")
print(df_clean.head(10))

output_csv = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_preprocessed.csv")
df_clean.to_csv(output_csv, index=False)
print(f"\nPreprocessed dataset successfully exported to: {output_csv}")
print("=" * 80)
