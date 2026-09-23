"""
LAB 2 - Step 3: Categorical Missing Values and Encoding Techniques
Topics Covered:
1. Handling missing values in categorical columns (Mode / Most Frequent).
2. Dummy Variables (Pandas get_dummies):
   - Creating binary indicator columns.
   - Avoiding the 'Dummy Variable Trap' (multicollinearity) via drop_first=True.
3. One-Hot Encoding (Scikit-Learn OneHotEncoder):
   - Transforming nominal categories into sparse/dense indicator matrices.
   - Handling unknown test categories cleanly.
4. Label Encoding vs Ordinal Encoding (Scikit-Learn):
   - LabelEncoder: Converting 1D categorical target vectors into integer IDs (0 to k-1).
   - OrdinalEncoder: Preserving intrinsic hierarchical order (e.g. Bachelors < Masters < PhD).
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

print("=" * 80)
print("LAB 2 - PART 3: CATEGORICAL DATA HANDLING & ENCODING")
print("=" * 80)

dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_raw.csv")
df_raw = pd.read_csv(dataset_path)

cat_cols = ["Department", "Education_Level", "Remote_Work", "Performance_Rating"]
print("Original Categorical Features (Sample):")
print(df_raw[cat_cols].head(8))

# -----------------------------------------------------------------------------
# 1. IMPUTING MISSING CATEGORICAL VALUES (MODE / MOST FREQUENT)
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("1. IMPUTING MISSING CATEGORICAL VALUES")
print("-" * 50)
df_clean_cat = df_raw[cat_cols].copy()

for col in cat_cols:
    mode_val = df_clean_cat[col].mode()[0]
    df_clean_cat[col] = df_clean_cat[col].fillna(mode_val)
    print(f"Feature: '{col}' -> Imputed missing NaNs with Mode: '{mode_val}'")

print("\nCategorical Features After Mode Imputation (NaN count = 0):")
print(df_clean_cat.isnull().sum())

# -----------------------------------------------------------------------------
# 2. DUMMY VARIABLES (Pandas get_dummies)
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("2. DUMMY VARIABLES VIA PANDAS (get_dummies)")
print("-" * 50)

# Full dummy variables (k columns for k categories)
dummies_full = pd.get_dummies(df_clean_cat["Department"], prefix="Dept", dtype=int)
print("Full Dummy Variables (Dept):\n", dummies_full.head(5))

# Dummy Variable Trap prevention: drop_first=True (k-1 columns)
dummies_no_trap = pd.get_dummies(df_clean_cat["Department"], prefix="Dept", drop_first=True, dtype=int)
print("\nDummy Variables with drop_first=True (Avoids Multicollinearity):\n", dummies_no_trap.head(5))

# -----------------------------------------------------------------------------
# 3. ONE-HOT ENCODING (Scikit-Learn OneHotEncoder)
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("3. ONE-HOT ENCODING VIA SCIKIT-LEARN (OneHotEncoder)")
print("-" * 50)

ohe = OneHotEncoder(drop='first', sparse_output=False)
ohe_transformed = ohe.fit_transform(df_clean_cat[["Department", "Remote_Work"]])
ohe_feature_names = ohe.get_feature_names_out(["Department", "Remote_Work"])

df_ohe = pd.DataFrame(ohe_transformed, columns=ohe_feature_names)
print(f"One-Hot Encoded Columns: {list(ohe_feature_names)}")
print(df_ohe.head(5))

# -----------------------------------------------------------------------------
# 4. ORDINAL ENCODING (For Ordered Categorical Variables)
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("4. ORDINAL ENCODING (Hierarchical Ordering)")
print("-" * 50)

# Education Level has a natural hierarchy: Bachelors < Masters < PhD
education_order = [["Bachelors", "Masters", "PhD"]]
ordinal_enc = OrdinalEncoder(categories=education_order)
df_clean_cat["Education_Ordinal"] = ordinal_enc.fit_transform(df_clean_cat[["Education_Level"]])

print("Ordinal Encoding mapping: Bachelors -> 0.0, Masters -> 1.0, PhD -> 2.0")
print(df_clean_cat[["Education_Level", "Education_Ordinal"]].drop_duplicates())

# -----------------------------------------------------------------------------
# 5. LABEL ENCODING (For 1D Target Variables)
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("5. LABEL ENCODING (Scikit-Learn LabelEncoder)")
print("-" * 50)

# Used for Target labels (e.g. Performance_Rating)
label_enc = LabelEncoder()
df_clean_cat["Performance_Encoded"] = label_enc.fit_transform(df_clean_cat["Performance_Rating"])

print("Classes identified by LabelEncoder:", label_enc.classes_)
for class_label, encoded_num in zip(label_enc.classes_, label_enc.transform(label_enc.classes_)):
    print(f" - Class '{class_label}' -> Encoded as integer: {encoded_num}")

print("\nComparison of Categorical Encoding Strategies:")
print(df_clean_cat[["Department", "Education_Level", "Education_Ordinal", "Performance_Rating", "Performance_Encoded"]].head(6))
print("=" * 80)
