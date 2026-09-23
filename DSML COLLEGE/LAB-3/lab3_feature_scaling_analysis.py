"""
====================================================================================================
LAB 3: FEATURE SCALING TECHNIQUES & DISTRIBUTION ANALYSIS
====================================================================================================
Objectives:
1. Master mathematical foundations of 4 core feature scaling techniques:
   - Min-Max Normalization [0, 1]
   - Z-Score Standardization (mean=0, std=1)
   - Mean Normalization (centered at 0)
   - Robust Scaling (Median & IQR based, immune to outliers)
2. Compare custom mathematical implementations with Scikit-Learn scalers.
3. Quantify Euclidean distance distortion in high-dimensional feature spaces.
4. Visualize the effect of scaling transformations on feature distributions.
====================================================================================================
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# --------------------------------------------------------------------------------------------------
# STEP 1: LOAD KAGGLE INSURANCE DATASET
# --------------------------------------------------------------------------------------------------
print("=" * 85)
print("STEP 1: LOADING KAGGLE MEDICAL INSURANCE DATASET")
print("=" * 85)

script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, "dataset", "insurance_kaggle.csv")

df = pd.read_csv(dataset_path)
print(f"Loaded Dataset: {df.shape[0]} samples x {df.shape[1]} features")
print("\nRaw Numeric Features Summary (Notice the drastic scale differences!):")
features = ["age", "bmi", "charges"]
print(df[features].describe().T[["mean", "std", "min", "25%", "50%", "75%", "max"]])

# --------------------------------------------------------------------------------------------------
# STEP 2: IMPLEMENTATION OF 4 SCALING TECHNIQUES (CUSTOM vs. SCIKIT-LEARN)
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 2: MATHEMATICAL FORMULATIONS vs. SCIKIT-LEARN SCALERS")
print("=" * 85)

charges_raw = df["charges"].values

# 1. Min-Max Normalization: (X - X_min) / (X_max - X_min)
min_val, max_val = charges_raw.min(), charges_raw.max()
charges_minmax_custom = (charges_raw - min_val) / (max_val - min_val)
charges_minmax_sklearn = MinMaxScaler().fit_transform(df[["charges"]]).flatten()
diff_minmax = np.max(np.abs(charges_minmax_custom - charges_minmax_sklearn))
print(f"1. Min-Max Scaling [0, 1]       -> Max difference vs Sklearn: {diff_minmax:.2e} (Exact Match)")

# 2. Z-Score Standardization: (X - mu) / sigma
mean_val, std_val = charges_raw.mean(), charges_raw.std(ddof=0)
charges_zscore_custom = (charges_raw - mean_val) / std_val
charges_zscore_sklearn = StandardScaler().fit_transform(df[["charges"]]).flatten()
diff_zscore = np.max(np.abs(charges_zscore_custom - charges_zscore_sklearn))
print(f"2. Z-Score Standardization      -> Max difference vs Sklearn: {diff_zscore:.2e} (Exact Match)")

# 3. Mean Normalization: (X - mu) / (X_max - X_min)
charges_mean_norm = (charges_raw - mean_val) / (max_val - min_val)
print(f"3. Mean Normalization           -> Range: [{charges_mean_norm.min():.3f}, {charges_mean_norm.max():.3f}], Mean: {charges_mean_norm.mean():.2e}")

# 4. Robust Scaling: (X - Median) / IQR
q25, q50, q75 = np.percentile(charges_raw, [25, 50, 75])
iqr = q75 - q25
charges_robust_custom = (charges_raw - q50) / iqr
charges_robust_sklearn = RobustScaler().fit_transform(df[["charges"]]).flatten()
diff_robust = np.max(np.abs(charges_robust_custom - charges_robust_sklearn))
print(f"4. Robust Scaling (IQR-based)   -> Max difference vs Sklearn: {diff_robust:.2e} (Exact Match)")

# --------------------------------------------------------------------------------------------------
# STEP 3: QUANTITATIVE DISTANCE DISTORTION DEMONSTRATION
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 3: EUCLIDEAN DISTANCE DISTORTION IN UNWEIGHTED MODELS (KNN / K-MEANS / SVM)")
print("=" * 85)

# Select two contrasting patient records
p1 = df[features].iloc[0].values  # Patient 1
p2 = df[features].iloc[1].values  # Patient 2

print(f"Patient 1 Raw Attributes: Age={p1[0]:.0f} yrs, BMI={p1[1]:.1f}, Charges=${p1[2]:,.2f}")
print(f"Patient 2 Raw Attributes: Age={p2[0]:.0f} yrs, BMI={p2[1]:.1f}, Charges=${p2[2]:,.2f}")

# Unscaled Distance
sq_diff_unscaled = (p1 - p2) ** 2
dist_unscaled = np.sqrt(np.sum(sq_diff_unscaled))
pct_age_unscaled = (sq_diff_unscaled[0] / np.sum(sq_diff_unscaled)) * 100
pct_bmi_unscaled = (sq_diff_unscaled[1] / np.sum(sq_diff_unscaled)) * 100
pct_charges_unscaled = (sq_diff_unscaled[2] / np.sum(sq_diff_unscaled)) * 100

print(f"\n--- UNSCALED RAW DISTANCE ---")
print(f"Total Euclidean Distance: {dist_unscaled:,.2f}")
print(f"  -> Age component squared diff     : {sq_diff_unscaled[0]:12,.2f} ({pct_age_unscaled:8.4f}% of total distance)")
print(f"  -> BMI component squared diff     : {sq_diff_unscaled[1]:12,.2f} ({pct_bmi_unscaled:8.4f}% of total distance)")
print(f"  -> Charges component squared diff : {sq_diff_unscaled[2]:12,.2f} ({pct_charges_unscaled:8.4f}% of total distance -> COMPLETELY DOMINATES!)")

# Scaled Distance (StandardScaler)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])
p1_s = df_scaled[0]
p2_s = df_scaled[1]

sq_diff_scaled = (p1_s - p2_s) ** 2
dist_scaled = np.sqrt(np.sum(sq_diff_scaled))
pct_age_scaled = (sq_diff_scaled[0] / np.sum(sq_diff_scaled)) * 100
pct_bmi_scaled = (sq_diff_scaled[1] / np.sum(sq_diff_scaled)) * 100
pct_charges_scaled = (sq_diff_scaled[2] / np.sum(sq_diff_scaled)) * 100

print(f"\n--- STANDARDIZED (Z-SCORE) DISTANCE ---")
print(f"Total Euclidean Distance: {dist_scaled:.4f}")
print(f"  -> Age component contribution     : {pct_age_scaled:6.2f}% (Balanced)")
print(f"  -> BMI component contribution     : {pct_bmi_scaled:6.2f}% (Balanced)")
print(f"  -> Charges component contribution : {pct_charges_scaled:6.2f}% (Balanced)")

# --------------------------------------------------------------------------------------------------
# STEP 4: VISUALIZATION OF DISTRIBUTION EFFECTS
# --------------------------------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Feature Scaling Transformations on Medical Charges Distribution", fontsize=15, fontweight='bold')

# Panel 1: Raw Charges (Right-skewed with long tail)
axes[0, 0].hist(charges_raw, bins=40, color='#1f77b4', edgecolor='black', alpha=0.7)
axes[0, 0].set_title(f"1. Raw Charges (Unscaled)\nMean=${charges_raw.mean():,.0f}, Std=${charges_raw.std():,.0f}", fontweight='bold')
axes[0, 0].set_xlabel("Dollar Amount ($)")
axes[0, 0].grid(True, linestyle=":", alpha=0.6)

# Panel 2: Min-Max Scaled [0, 1]
axes[0, 1].hist(charges_minmax_custom, bins=40, color='#ff7f0e', edgecolor='black', alpha=0.7)
axes[0, 1].set_title(f"2. Min-Max Normalization\nBound: [0.0, 1.0]", fontweight='bold')
axes[0, 1].set_xlabel("Normalized Value")
axes[0, 1].grid(True, linestyle=":", alpha=0.6)

# Panel 3: Z-Score Standardized (mu=0, sigma=1)
axes[1, 0].hist(charges_zscore_custom, bins=40, color='#2ca02c', edgecolor='black', alpha=0.7)
axes[1, 0].axvline(0, color='red', linestyle='--', label='Mean = 0')
axes[1, 0].set_title(f"3. Z-Score Standardization\nMean=0.00, Std Dev=1.00", fontweight='bold')
axes[1, 0].set_xlabel("Standard Deviations from Mean")
axes[1, 0].legend()
axes[1, 0].grid(True, linestyle=":", alpha=0.6)

# Panel 4: Robust Scaled (Median=0, IQR=1)
axes[1, 1].hist(charges_robust_custom, bins=40, color='#9467bd', edgecolor='black', alpha=0.7)
axes[1, 1].axvline(0, color='red', linestyle='--', label='Median = 0')
axes[1, 1].set_title(f"4. Robust Scaling (IQR-based)\nMedian=0.00, Outlier-Resistant", fontweight='bold')
axes[1, 1].set_xlabel("Interquartile Units")
axes[1, 1].legend()
axes[1, 1].grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
out_fig = os.path.join(script_dir, "feature_scaling_distributions.png")
plt.savefig(out_fig, dpi=300)
plt.close()

print(f"\nDistribution comparison figure saved to:\n -> {out_fig}")
print("=" * 85)
print("LAB 3 COMPLETED SUCCESSFULLY!")
print("=" * 85)
