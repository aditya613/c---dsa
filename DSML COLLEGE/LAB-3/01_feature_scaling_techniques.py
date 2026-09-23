"""
LAB 3 - Step 1: Feature Scaling Techniques Implementation
Topics Covered:
1. Understanding the necessity of feature scaling in machine learning.
2. Min-Max Normalization (Rescaling to [0, 1]):
   - Formula: X_norm = (X - X_min) / (X_max - X_min)
   - Custom implementation + Scikit-Learn MinMaxScaler
3. Standardization / Z-score Normalization (Mean = 0, Std = 1):
   - Formula: Z = (X - mu) / sigma
   - Custom implementation + Scikit-Learn StandardScaler
4. Mean Normalization:
   - Formula: X_mean_norm = (X - mu) / (X_max - X_min)
5. Robust Scaling (Outlier-resilient using Median & Interquartile Range):
   - Formula: X_robust = (X - Median) / IQR (where IQR = Q3 - Q1)
   - Scikit-Learn RobustScaler
6. Comparative statistical table of all scalers.
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler

print("=" * 80)
print("LAB 3 - PART 1: FEATURE SCALING METHODS IMPLEMENTATION")
print("=" * 80)

dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "customer_profiles.csv")
df = pd.read_csv(dataset_path)

print(f"Dataset loaded ({len(df)} samples). Features summary before scaling:")
feature_cols = ["Age", "Annual_Income", "Credit_Score", "Online_Purchases"]
print(df[feature_cols].describe().round(2))

# -----------------------------------------------------------------------------
# 1. MIN-MAX NORMALIZATION
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("1. MIN-MAX NORMALIZATION (Scales to [0, 1])")
print("-" * 50)

# Custom mathematical formulation
income_raw = df["Annual_Income"].values
income_min = income_raw.min()
income_max = income_raw.max()
income_minmax_custom = (income_raw - income_min) / (income_max - income_min)

# Scikit-Learn MinMaxScaler
min_max_scaler = MinMaxScaler(feature_range=(0, 1))
income_minmax_sklearn = min_max_scaler.fit_transform(df[["Annual_Income"]]).flatten()

print(f"Custom formula matches Sklearn? {np.allclose(income_minmax_custom, income_minmax_sklearn)}")
print(f"Original Income range: [{income_min}, {income_max}]")
print(f"Min-Max Scaled range:  [{income_minmax_sklearn.min():.4f}, {income_minmax_sklearn.max():.4f}]")

# -----------------------------------------------------------------------------
# 2. STANDARDIZATION (Z-SCORE NORMALIZATION)
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("2. STANDARDIZATION / Z-SCORE (Mean = 0, Std = 1)")
print("-" * 50)

# Custom mathematical formulation
income_mu = income_raw.mean()
income_sigma = income_raw.std(ddof=0)  # Population std (matching sklearn)
income_z_custom = (income_raw - income_mu) / income_sigma

# Scikit-Learn StandardScaler
std_scaler = StandardScaler()
income_z_sklearn = std_scaler.fit_transform(df[["Annual_Income"]]).flatten()

print(f"Custom Z-score matches Sklearn? {np.allclose(income_z_custom, income_z_sklearn)}")
print(f"Standardized Mean: {income_z_sklearn.mean():.6f} (~0)")
print(f"Standardized Std:  {income_z_sklearn.std():.6f} (~1)")

# -----------------------------------------------------------------------------
# 3. MEAN NORMALIZATION
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("3. MEAN NORMALIZATION (Centers at 0, bounded by range)")
print("-" * 50)

# Formula: (X - Mean) / (Max - Min)
income_mean_norm = (income_raw - income_mu) / (income_max - income_min)
print(f"Mean Normalized Mean:  {income_mean_norm.mean():.6f} (~0)")
print(f"Mean Normalized Range: [{income_mean_norm.min():.4f}, {income_mean_norm.max():.4f}]")

# -----------------------------------------------------------------------------
# 4. ROBUST SCALER (Outlier Robust)
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("4. ROBUST SCALING (Using Median and Interquartile Range Q3 - Q1)")
print("-" * 50)

robust_scaler = RobustScaler()
income_robust = robust_scaler.fit_transform(df[["Annual_Income"]]).flatten()

q1 = np.percentile(income_raw, 25)
median = np.median(income_raw)
q3 = np.percentile(income_raw, 75)
iqr = q3 - q1

print(f"Median: {median}, Q1: {q1}, Q3: {q3}, IQR: {iqr}")
print(f"Robust Scaled Median: {np.median(income_robust):.4f} (Exactly 0)")
print(f"Outlier sample (Index 19, Income=$450,000):")
print(f" - Min-Max Value:     {income_minmax_sklearn[-1]:.4f} (Pushed remaining 95% data into tiny [0, 0.35] region)")
print(f" - Standardized Z:    {income_z_sklearn[-1]:.4f} (Huge Z-score of +3.5+)")
print(f" - Robust Scaled:     {income_robust[-1]:.4f} (Preserves relative scale of non-outliers)")

# -----------------------------------------------------------------------------
# 5. CONSOLIDATED SCALED DATAFRAME
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("5. CONSOLIDATED COMPARISON TABLE")
print("-" * 50)

comparison_df = pd.DataFrame({
    "Raw_Income": income_raw,
    "MinMax_[0,1]": income_minmax_sklearn.round(3),
    "Z_Score": income_z_sklearn.round(3),
    "Mean_Normalized": income_mean_norm.round(3),
    "Robust_IQR": income_robust.round(3)
})
print(comparison_df.head(10))
print("=" * 80)
