"""
LAB 3 - Step 2: Observing the Effect of Feature Scaling on Data Distribution
Topics Covered:
1. Plotting histograms and KDE distributions across scaling techniques.
2. Observing changes in:
   - Centering (Mean = 0 vs Median = 0 vs Min = 0)
   - Spread and scale range ([0, 1] vs unit variance vs IQR)
   - Outlier compression and preservation
3. 2D Distance Distortion Analysis:
   - Why unscaled features ruin distance-based algorithms (KNN, K-Means, SVM).
   - How feature scaling equalizes Euclidean distance contributions.
4. Exporting comprehensive multi-panel visual comparison to PNG.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

print("=" * 80)
print("LAB 3 - PART 2: VISUALIZING DISTRIBUTION EFFECTS OF SCALING")
print("=" * 80)

dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "customer_profiles.csv")
df = pd.read_csv(dataset_path)

# Extract features
income = df[["Annual_Income"]]
age = df[["Age"]]

# Apply scalers
minmax = MinMaxScaler()
std = StandardScaler()
robust = RobustScaler()

df["Income_MinMax"] = minmax.fit_transform(income)
df["Income_Std"] = std.fit_transform(income)
df["Income_Robust"] = robust.fit_transform(income)

df["Age_MinMax"] = minmax.fit_transform(age)
df["Age_Std"] = std.fit_transform(age)

# -----------------------------------------------------------------------------
# CREATE 4-PANEL DISTRIBUTION VISUALIZATION
# -----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Raw Distribution
axes[0, 0].hist(df["Annual_Income"] / 1000, bins=10, color='#3b82f6', edgecolor='black', alpha=0.7)
axes[0, 0].set_title("1. Raw Annual Income (in Thousands $)", fontsize=11, fontweight='bold')
axes[0, 0].set_xlabel("Income ($k)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].grid(True, linestyle='--', alpha=0.5)

# 2. Min-Max Normalization Distribution
axes[0, 1].hist(df["Income_MinMax"], bins=10, color='#10b981', edgecolor='black', alpha=0.7)
axes[0, 1].set_title("2. Min-Max Normalization [0, 1]", fontsize=11, fontweight='bold')
axes[0, 1].set_xlabel("Scaled Value (Bounded strictly 0 to 1)")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].grid(True, linestyle='--', alpha=0.5)

# 3. Standardization (Z-score) Distribution
axes[1, 0].hist(df["Income_Std"], bins=10, color='#f59e0b', edgecolor='black', alpha=0.7)
axes[1, 0].axvline(0, color='red', linestyle='--', linewidth=1.5, label='Mean = 0')
axes[1, 0].set_title("3. Standardization / Z-Score (Mean=0, Std=1)", fontsize=11, fontweight='bold')
axes[1, 0].set_xlabel("Standard Deviations from Mean")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].legend()
axes[1, 0].grid(True, linestyle='--', alpha=0.5)

# 4. Robust Scaler Distribution
axes[1, 1].hist(df["Income_Robust"], bins=10, color='#8b5cf6', edgecolor='black', alpha=0.7)
axes[1, 1].axvline(0, color='red', linestyle='--', linewidth=1.5, label='Median = 0')
axes[1, 1].set_title("4. Robust Scaler (Median=0, Scale=IQR)", fontsize=11, fontweight='bold')
axes[1, 1].set_xlabel("IQR Units from Median")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].legend()
axes[1, 1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
dist_img = os.path.join(os.path.dirname(__file__), "feature_scaling_distributions.png")
plt.savefig(dist_img, dpi=200)
plt.close()
print(f"Distribution comparison figure saved to: {dist_img}")

# -----------------------------------------------------------------------------
# 2D DISTANCE DEMONSTRATION (Euclidean distance impact)
# -----------------------------------------------------------------------------
print("\n--- Euclidean Distance Impact Demonstration ---")
p1_idx, p2_idx = 0, 1  # Customer C101 (24 yrs, $32k) vs C102 (45 yrs, $115k)

# Raw Euclidean distance
raw_diff_age = df.loc[p1_idx, "Age"] - df.loc[p2_idx, "Age"]
raw_diff_inc = df.loc[p1_idx, "Annual_Income"] - df.loc[p2_idx, "Annual_Income"]
raw_dist = np.sqrt(raw_diff_age**2 + raw_diff_inc**2)

# Scaled Euclidean distance
std_diff_age = df.loc[p1_idx, "Age_Std"] - df.loc[p2_idx, "Age_Std"]
std_diff_inc = df.loc[p1_idx, "Income_Std"] - df.loc[p2_idx, "Income_Std"]
std_dist = np.sqrt(std_diff_age**2 + std_diff_inc**2)

print(f"Customer 1: Age={df.loc[p1_idx, 'Age']}, Income=${df.loc[p1_idx, 'Annual_Income']}")
print(f"Customer 2: Age={df.loc[p2_idx, 'Age']}, Income=${df.loc[p2_idx, 'Annual_Income']}")
print(f"\nUnscaled Raw Distance: {raw_dist:.2f}")
print(f" -> Age component contribution:    {(raw_diff_age**2 / raw_dist**2)*100:.4f}%")
print(f" -> Income component contribution: {(raw_diff_inc**2 / raw_dist**2)*100:.4f}% (COMPLETELY DOMINATES!)")

print(f"\nStandardized Distance: {std_dist:.4f}")
print(f" -> Age component contribution:    {(std_diff_age**2 / std_dist**2)*100:.2f}%")
print(f" -> Income component contribution: {(std_diff_inc**2 / std_dist**2)*100:.2f}% (BALANCED!)")
print("=" * 80)
