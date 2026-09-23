"""
LAB 1 - Part 1: Exploration of Python Libraries for Data Handling and Machine Learning
Libraries covered:
1. NumPy: High-performance multi-dimensional arrays, vectorization, and linear algebra.
2. Pandas: Data structures (Series, DataFrame), tabular data manipulation, and aggregation.
3. Matplotlib: Data visualization, plotting graphs, histograms, and scatter plots.
4. Scikit-learn: Machine learning tools for preprocessing, model building, and evaluation.
"""

import os
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("=" * 80)
print("LAB 1 - PART 1: EXPLORATION OF CORE PYTHON DATA SCIENCE & ML LIBRARIES")
print("=" * 80)

# -----------------------------------------------------------------------------
# 1. NUMPY: Numerical Python
# -----------------------------------------------------------------------------
print("\n[1] EXPLORING NUMPY")
print("-" * 40)

# Array creation & shapes
arr1d = np.array([10, 20, 30, 40, 50])
arr2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)

print(f"1D Array: {arr1d} | Shape: {arr1d.shape} | Dtype: {arr1d.dtype}")
print(f"2D Array:\n{arr2d}\nShape: {arr2d.shape} | Dimensions: {arr2d.ndim}")

# Vectorized operations (Element-wise arithmetic without loops)
squared = arr1d ** 2
print(f"Vectorized Squaring (arr1d ** 2): {squared}")

# Broadcasting & Statistical methods
matrix_a = np.arange(1, 10).reshape(3, 3)
vector_b = np.array([10, 20, 30])
broadcasted_sum = matrix_a + vector_b

print(f"Matrix A (3x3):\n{matrix_a}")
print(f"Vector B (3,): {vector_b}")
print(f"Broadcasted Sum (A + B):\n{broadcasted_sum}")
print(f"Statistical Summary -> Mean: {matrix_a.mean():.2f}, Sum: {matrix_a.sum()}, Std: {matrix_a.std():.2f}")

# Matrix multiplication
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
mat_prod = np.dot(mat1, mat2)
print(f"Matrix Dot Product:\n{mat_prod}")


# -----------------------------------------------------------------------------
# 2. PANDAS: Data Analysis & Manipulation
# -----------------------------------------------------------------------------
print("\n[2] EXPLORING PANDAS")
print("-" * 40)

# Pandas Series
sales_series = pd.Series([120, 300, 250, 400], index=['Q1', 'Q2', 'Q3', 'Q4'], name="Sales_2026")
print("Pandas Series:")
print(sales_series)

# Pandas DataFrame
data = {
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Aditya", "Aarav", "Diya", "Kabir", "Meera"],
    "Department": ["CSE", "ECE", "CSE", "IT", "CSE"],
    "CGPA": [9.2, 8.5, 9.6, 7.8, 8.9],
    "Placement_Status": ["Placed", "Placed", "Placed", "Pending", "Placed"]
}
df = pd.DataFrame(data)
print("\nStudent DataFrame:")
print(df)

# DataFrame inspection and filtering
print("\nSummary Statistics:")
print(df.describe())

high_cgpa_students = df[df["CGPA"] >= 9.0]
print("\nStudents with CGPA >= 9.0:")
print(high_cgpa_students[["Name", "Department", "CGPA"]])

# Groupby aggregation
dept_summary = df.groupby("Department")["CGPA"].agg(["count", "mean", "max"])
print("\nDepartment-wise CGPA Summary:")
print(dept_summary)


# -----------------------------------------------------------------------------
# 3. MATPLOTLIB: Data Visualization
# -----------------------------------------------------------------------------
print("\n[3] EXPLORING MATPLOTLIB")
print("-" * 40)

# Generate synthetic data for visualization
np.random.seed(42)
x_vals = np.linspace(0, 10, 50)
y_sine = np.sin(x_vals)
scatter_x = np.random.normal(5, 2, 60)
scatter_y = 2.5 * scatter_x + np.random.normal(0, 2, 60)

# Create a multi-panel figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Line plot
axes[0].plot(x_vals, y_sine, color='#0284c7', linewidth=2, label='sin(x)')
axes[0].set_title('Trigonometric Function (Sine Wave)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('X (radians)')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend()

# Plot 2: Scatter plot
axes[1].scatter(scatter_x, scatter_y, color='#16a34a', alpha=0.7, edgecolors='k', label='Data points')
axes[1].set_title('Feature Correlation Scatter Plot', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Independent Variable X')
axes[1].set_ylabel('Dependent Variable Y')
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].legend()

plt.tight_layout()
output_img = os.path.join(os.path.dirname(__file__), "lib_exploration_plot.png")
plt.savefig(output_img, dpi=200)
plt.close()
print(f"Visualization successfully generated and saved to: {output_img}")


# -----------------------------------------------------------------------------
# 4. SCIKIT-LEARN: Machine Learning Pipeline
# -----------------------------------------------------------------------------
print("\n[4] EXPLORING SCIKIT-LEARN")
print("-" * 40)

# Generating a simple binary classification dataset
np.random.seed(42)
num_samples = 120
features = np.random.randn(num_samples, 2)
# Target label: 1 if feature sum > 0 else 0
labels = (features[:, 0] + features[:, 1] > 0).astype(int)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Training: Logistic Regression
clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)

# Predictions and Evaluation
y_pred = clf.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)

print(f"Total Samples: {num_samples} (Train: {len(X_train)}, Test: {len(X_test)})")
print(f"Model Learned Coefficients: {clf.coef_[0]}, Intercept: {clf.intercept_[0]:.4f}")
print(f"Test Set Accuracy: {acc * 100:.2f}%")

print("\n" + "=" * 80)
print("EXPLORATION COMPLETE: All libraries verified and operational.")
print("=" * 80)
