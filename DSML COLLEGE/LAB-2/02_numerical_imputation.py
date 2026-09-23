"""
LAB 2 - Step 2: Numerical Missing Data Imputation (Mean, Median, Mode)
Topics Covered:
1. Identifying numerical features with missing values (NaNs).
2. Mean Imputation:
   - Suitable for normally distributed features without extreme outliers.
   - Preserves feature mean but reduces variance.
3. Median Imputation:
   - Robust to skewed distributions and extreme outliers.
4. Mode (Most Frequent) Imputation:
   - Imputes discrete or count-based numerical values with highest occurrence.
5. Dual Implementation:
   - Approach A: Pandas fillna() methods.
   - Approach B: Scikit-learn SimpleImputer classes.
6. Before-and-after variance and distribution comparison.
"""

import os
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

print("=" * 80)
print("LAB 2 - PART 2: NUMERICAL MISSING DATA IMPUTATION")
print("=" * 80)

dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_raw.csv")
df_raw = pd.read_csv(dataset_path)

print("Original Data - Numerical Columns:")
num_cols = ["Experience_Years", "Salary"]
print(df_raw[num_cols].head(10))

# -----------------------------------------------------------------------------
# 1. PANDAS-BASED IMPUTATION
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("1. IMPUTATION USING PANDAS (.fillna())")
print("-" * 50)

# Calculate statistics
exp_mean = df_raw["Experience_Years"].mean()
exp_median = df_raw["Experience_Years"].median()
exp_mode = df_raw["Experience_Years"].mode()[0]

salary_mean = df_raw["Salary"].mean()
salary_median = df_raw["Salary"].median()
salary_mode = df_raw["Salary"].mode()[0]

print(f"Experience_Years -> Mean: {exp_mean:.2f}, Median: {exp_median:.2f}, Mode: {exp_mode:.2f}")
print(f"Salary           -> Mean: {salary_mean:.2f}, Median: {salary_median:.2f}, Mode: {salary_mode:.2f}")

# Mean Imputation on Salary
df_mean_imp = df_raw.copy()
df_mean_imp["Salary_Mean_Imputed"] = df_mean_imp["Salary"].fillna(salary_mean)

# Median Imputation on Experience_Years (robust against outliers)
df_median_imp = df_raw.copy()
df_median_imp["Experience_Median_Imputed"] = df_median_imp["Experience_Years"].fillna(exp_median)

# Mode Imputation on Experience_Years
df_mode_imp = df_raw.copy()
df_mode_imp["Experience_Mode_Imputed"] = df_mode_imp["Experience_Years"].fillna(exp_mode)

print("\nSample Comparisons (Pandas fillna):")
preview_df = pd.DataFrame({
    "Original_Experience": df_raw["Experience_Years"],
    "Median_Imputed_Exp": df_median_imp["Experience_Median_Imputed"],
    "Mode_Imputed_Exp": df_mode_imp["Experience_Mode_Imputed"],
    "Original_Salary": df_raw["Salary"],
    "Mean_Imputed_Salary": df_mean_imp["Salary_Mean_Imputed"].round(1)
})
print(preview_df.head(10))

# -----------------------------------------------------------------------------
# 2. SCIKIT-LEARN SIMPLEIMPUTER
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("2. IMPUTATION USING SCIKIT-LEARN (SimpleImputer)")
print("-" * 50)

# Strategy 1: Mean
mean_imputer = SimpleImputer(strategy='mean')
salary_imputed_sklearn = mean_imputer.fit_transform(df_raw[["Salary"]])
print(f"SimpleImputer(strategy='mean') learned statistic: {mean_imputer.statistics_[0]:.2f}")

# Strategy 2: Median
median_imputer = SimpleImputer(strategy='median')
exp_imputed_sklearn = median_imputer.fit_transform(df_raw[["Experience_Years"]])
print(f"SimpleImputer(strategy='median') learned statistic: {median_imputer.statistics_[0]:.2f}")

# Strategy 3: Most Frequent (Mode)
mode_imputer = SimpleImputer(strategy='most_frequent')
exp_mode_sklearn = mode_imputer.fit_transform(df_raw[["Experience_Years"]])
print(f"SimpleImputer(strategy='most_frequent') learned statistic: {mode_imputer.statistics_[0]:.2f}")

# -----------------------------------------------------------------------------
# 3. STATISTICAL COMPARISON & VARIANCE IMPACT
# -----------------------------------------------------------------------------
print("\n" + "-" * 50)
print("3. STATISTICAL IMPACT OF IMPUTATION")
print("-" * 50)
stats_comp = pd.DataFrame({
    "Metric": ["Count", "Mean", "Std Dev", "Min", "Max"],
    "Salary_Original": [
        df_raw["Salary"].count(),
        df_raw["Salary"].mean(),
        df_raw["Salary"].std(),
        df_raw["Salary"].min(),
        df_raw["Salary"].max()
    ],
    "Salary_Mean_Imputed": [
        df_mean_imp["Salary_Mean_Imputed"].count(),
        df_mean_imp["Salary_Mean_Imputed"].mean(),
        df_mean_imp["Salary_Mean_Imputed"].std(),
        df_mean_imp["Salary_Mean_Imputed"].min(),
        df_mean_imp["Salary_Mean_Imputed"].max()
    ]
})
print(stats_comp.round(2))
print("\nKey Takeaway: Mean imputation preserves the sample mean, but artificially compresses the standard deviation (variance).")
print("=" * 80)
