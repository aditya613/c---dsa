"""
LAB 2 - Step 1: Dataset Inspection and Missing Data Visualization
Topics Covered:
1. Loading tabular datasets using Pandas.
2. Structural inspection: shape, dtypes, non-null counts via info().
3. Summary statistics via describe().
4. Identifying missing data: isnull().sum() and percentage computation.
5. Graphical visualization of missingness patterns using Matplotlib:
   - Missing value counts bar plot
   - Missing data matrix heatmap showing record-level sparsity
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 80)
print("LAB 2 - PART 1: DATASET INSPECTION & MISSINGNESS VISUALIZATION")
print("=" * 80)

# 1. Load the Dataset
dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "employee_data_raw.csv")
df = pd.read_csv(dataset_path)

print(f"Dataset successfully loaded from: {dataset_path}")
print(f"Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns\n")

# 2. Display First 5 Records
print("--- First 5 Records ---")
print(df.head())

# 3. Structural Information
print("\n--- DataFrame Information ---")
print(df.info())

# 4. Statistical Summary of Numerical Features
print("\n--- Numerical Summary Statistics ---")
print(df.describe())

# 5. Missing Value Analysis
print("\n--- Missing Value Count and Percentage per Column ---")
missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df)) * 100
missing_df = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage (%)": missing_percent.round(2)
})
print(missing_df[missing_df["Missing_Count"] > 0])

# 6. Visualization of Missingness
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Missing values count bar chart
cols_with_missing = missing_count[missing_count > 0]
ax1.bar(cols_with_missing.index, cols_with_missing.values, color='#ef4444', alpha=0.85, edgecolor='black')
ax1.set_title("Missing Values Count by Feature", fontsize=12, fontweight='bold')
ax1.set_xlabel("Feature Name")
ax1.set_ylabel("Number of NaN Entries")
ax1.grid(axis='y', linestyle='--', alpha=0.6)
for i, v in enumerate(cols_with_missing.values):
    ax1.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

# Plot 2: Missing Data Heatmap Matrix (1 for Missing, 0 for Present)
missing_matrix = df.isnull().astype(int)
im = ax2.imshow(missing_matrix, cmap='YlOrRd', aspect='auto', interpolation='nearest')
ax2.set_title("Missing Data Sparsity Matrix (Red = Missing)", fontsize=12, fontweight='bold')
ax2.set_xticks(range(len(df.columns)))
ax2.set_xticklabels(df.columns, rotation=45, ha='right', fontsize=9)
ax2.set_ylabel("Sample Row Index")

plt.tight_layout()
output_img = os.path.join(os.path.dirname(__file__), "missing_data_visualization.png")
plt.savefig(output_img, dpi=200)
plt.close()

print(f"\nMissing data visual plot successfully saved to: {output_img}")
print("=" * 80)
