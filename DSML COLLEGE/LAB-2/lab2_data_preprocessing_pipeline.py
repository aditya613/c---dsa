"""
====================================================================================================
LAB 2: DATA PREPROCESSING, IMPUTATION & LEAK-FREE PIPELINES
====================================================================================================
Objectives:
1. Inspect, diagnose, and visualize real-world missing data patterns on the Kaggle Titanic dataset.
2. Implement Numerical Imputation (Mean, Median) and compare statistical impacts.
3. Implement Categorical Imputation (Mode) and Encoding (One-Hot Encoding, Dummy Trap resolution).
4. Build an end-to-end, leak-free Scikit-Learn ColumnTransformer pipeline.
5. Export clean, ML-ready feature matrices for downstream predictive modeling.
====================================================================================================
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

# --------------------------------------------------------------------------------------------------
# STEP 1: LOAD & DIAGNOSE RAW KAGGLE DATASET
# --------------------------------------------------------------------------------------------------
print("=" * 85)
print("STEP 1: LOADING & DIAGNOSING REAL-WORLD KAGGLE TITANIC DATASET")
print("=" * 85)

script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, "dataset", "titanic_kaggle.csv")

df_raw = pd.read_csv(dataset_path)
print(f"Loaded Raw Dataset: {df_raw.shape[0]} samples x {df_raw.shape[1]} features")
print("\nRaw Data Sample:")
print(df_raw[["PassengerId", "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]].head())

# Missing Data Quantification
missing_counts = df_raw.isnull().sum()
missing_pct = (missing_counts / len(df_raw)) * 100
missing_report = pd.DataFrame({"Missing Entries": missing_counts, "Percentage (%)": missing_pct})
print("\nMissing Data Summary:")
print(missing_report[missing_report["Missing Entries"] > 0])

# Visualize Missing Data Matrix
plt.figure(figsize=(10, 5))
plt.imshow(df_raw.isnull(), cmap='magma', aspect='auto')
plt.title("Kaggle Titanic Missing Data Heatmap (Bright = Missing NaN)", fontsize=12, fontweight='bold')
plt.xlabel("Feature Index")
plt.ylabel("Sample Index")
plt.xticks(range(df_raw.shape[1]), df_raw.columns, rotation=45, ha='right')
plt.tight_layout()
heatmap_path = os.path.join(script_dir, "missing_data_visualization.png")
plt.savefig(heatmap_path, dpi=300)
plt.close()
print(f"Missingness visualization saved to: {heatmap_path}")

# --------------------------------------------------------------------------------------------------
# STEP 2: STATISTICAL IMPUTATION METHODS COMPARISON
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 2: NUMERICAL IMPUTATION COMPARISONS (MEAN vs. MEDIAN)")
print("=" * 85)

age_original = df_raw["Age"].dropna()
age_mean_val = df_raw["Age"].mean()
age_median_val = df_raw["Age"].median()

print(f"Original Observed Age -> Mean: {age_mean_val:.2f}, Median: {age_median_val:.2f}, Std: {age_original.std():.2f}")

# Impute with Mean
imputer_mean = SimpleImputer(strategy='mean')
age_imputed_mean = imputer_mean.fit_transform(df_raw[["Age"]])

# Impute with Median
imputer_median = SimpleImputer(strategy='median')
age_imputed_median = imputer_median.fit_transform(df_raw[["Age"]])

print(f"After Mean Imputation   -> Mean: {age_imputed_mean.mean():.2f}, Std Dev: {age_imputed_mean.std():.2f} (Variance artificially reduced)")
print(f"After Median Imputation -> Median: {np.median(age_imputed_median):.2f}, Std Dev: {age_imputed_median.std():.2f} (Robust against skewness)")

# Mode Imputation for Categorical Feature (Embarked)
most_freq_embarked = df_raw["Embarked"].mode()[0]
print(f"\nCategorical Mode for 'Embarked': '{most_freq_embarked}' (Frequency: {(df_raw['Embarked'] == most_freq_embarked).sum()})")

# --------------------------------------------------------------------------------------------------
# STEP 3: CATEGORICAL ENCODING & THE DUMMY VARIABLE TRAP
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 3: CATEGORICAL ENCODING & THE DUMMY VARIABLE TRAP")
print("=" * 85)

# Demonstrate Dummy Variable Trap on 'Sex' and 'Embarked'
print("Demonstrating Pandas get_dummies with and without 'drop_first':")
dummy_raw = pd.get_dummies(df_raw["Embarked"], prefix="Port")
print("Without drop_first (Collinear / Dummy Variable Trap):\n", dummy_raw.head(3))

dummy_safe = pd.get_dummies(df_raw["Embarked"], prefix="Port", drop_first=True)
print("\nWith drop_first=True (Safe, Multicollinearity Avoided):\n", dummy_safe.head(3))
print("-> Note: Port_C is dropped as the reference baseline; if Port_Q=0 and Port_S=0, it implies Port_C.")

# --------------------------------------------------------------------------------------------------
# STEP 4: PRODUCTION-GRADE, LEAK-FREE PIPELINE VIA COLUMNTRANSFORMER
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 4: END-TO-END LEAK-FREE PREPROCESSING PIPELINE")
print("=" * 85)

# Separate Target and Features
target_col = "Survived"
X = df_raw.drop(columns=["PassengerId", "Name", "Ticket", "Cabin", target_col])
y = df_raw[target_col]

# CRITICAL BEST PRACTICE: Train/Test Split BEFORE fitting any imputer or scaler to prevent data leakage!
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

numerical_cols = ["Age", "Fare", "SibSp", "Parch"]
categorical_nominal_cols = ["Sex", "Embarked"]
ordinal_cols = ["Pclass"]

print(f"Training Set Samples: {len(X_train)}, Testing Set Samples: {len(X_test)}")
print(f"Numerical Features    : {numerical_cols}")
print(f"Categorical Features  : {categorical_nominal_cols}")
print(f"Ordinal Features      : {ordinal_cols}")

# Numerical Pipeline: Median Imputation -> Z-Score Scaling
num_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Categorical Nominal Pipeline: Mode Imputation -> One-Hot Encoding (drop first column)
cat_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))
])

# Ordinal Pipeline: Mode Imputation -> Pass-through or OrdinalEncoder
ord_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ordinal', OrdinalEncoder())
])

# Combine all transformations into a single ColumnTransformer
preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, numerical_cols),
    ('cat', cat_pipeline, categorical_nominal_cols),
    ('ord', ord_pipeline, ordinal_cols)
])

# Fit ONLY on X_train, then transform both X_train and X_test
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Extract generated column names
ohe_feature_names = list(preprocessor.named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(categorical_nominal_cols))
all_column_names = numerical_cols + ohe_feature_names + ordinal_cols

# Convert back to clean DataFrames for demonstration and export
df_train_clean = pd.DataFrame(X_train_processed, columns=all_column_names)
df_train_clean["Target_Survived"] = y_train.values

print("\n" + "=" * 85)
print("FINAL ML-READY PREPROCESSED DATASET")
print("=" * 85)
print(f"Processed Feature Matrix Shape: {df_train_clean.shape} (Zero NaNs remaining!)")
print("\nFirst 5 Processed Records:")
print(df_train_clean.head())

out_csv = os.path.join(script_dir, "dataset", "titanic_preprocessed.csv")
df_train_clean.to_csv(out_csv, index=False)
print(f"\nClean preprocessed dataset saved to:\n -> {out_csv}")
print("=" * 85)
print("LAB 2 COMPLETED SUCCESSFULLY!")
print("=" * 85)
