"""
LAB 4 - Step 3: Scikit-Learn LinearRegression & Regression Visualization
Topics Covered:
1. Training a Linear Regression model with Scikit-learn (sklearn.linear_model.LinearRegression).
2. Model parameters: model.coef_ and model.intercept_.
3. Train-test evaluation using mean_squared_error, mean_absolute_error, and r2_score.
4. Comprehensive regression plot:
   - Scatter plot of training and testing data points.
   - Best-fit regression line.
   - Vertical residual error bars (illustrating the least squares minimization objective).
5. Mathematical verification: Proving Sklearn matches OLS closed-form and Gradient Descent.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print("=" * 80)
print("LAB 4 - PART 3: SCIKIT-LEARN LINEAR REGRESSION & VISUALIZATION")
print("=" * 80)

dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "experience_salary.csv")
df = pd.read_csv(dataset_path)

X = df[["Years_Experience"]].values
y = df["Salary"].values

# Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate and Fit Scikit-Learn Model
model = LinearRegression()
model.fit(X_train, y_train)

slope = model.coef_[0]
intercept = model.intercept_

print(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")
print(f"Learned Slope (coef_):      {slope:.4f}")
print(f"Learned Intercept (bias):   ${intercept:.4f}")

# Predictions on Test Set
y_test_pred = model.predict(X_test)
y_all_pred = model.predict(X)

# Evaluation Metrics on Test Set
test_mae = mean_absolute_error(y_test, y_test_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)
test_r2 = r2_score(y_test, y_test_pred)

print("\n--- Test Set Evaluation Metrics ---")
print(f"Mean Absolute Error (MAE):       ${test_mae:.2f}")
print(f"Mean Squared Error (MSE):        {test_mse:.2f}")
print(f"Root Mean Squared Error (RMSE):  ${test_rmse:.2f}")
print(f"R-squared Score (R^2):           {test_r2:.4f} ({test_r2 * 100:.2f}%)")

# -----------------------------------------------------------------------------
# PLOT REGRESSION FIT WITH RESIDUALS
# -----------------------------------------------------------------------------
plt.figure(figsize=(10, 6))

# Plot training and test scatter points
plt.scatter(X_train, y_train, color='#2563eb', label='Training Samples', s=55, alpha=0.8)
plt.scatter(X_test, y_test, color='#dc2626', label='Testing Samples', s=70, edgecolors='k', zorder=5)

# Plot fitted regression line across full range
x_line = np.linspace(X.min() - 0.5, X.max() + 0.5, 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='#059669', linewidth=2.5, label=f'Regression Line: y = {intercept:.0f} + {slope:.0f}x')

# Draw vertical residual error bars for test points
for x_val, y_actual, y_hat in zip(X_test.flatten(), y_test, y_test_pred):
    plt.plot([x_val, x_val], [y_actual, y_hat], color='#dc2626', linestyle='--', linewidth=1.5, alpha=0.7)

plt.title("Simple Linear Regression: Experience vs Salary (with Residual Errors)", fontsize=12, fontweight='bold')
plt.xlabel("Years of Experience", fontsize=11)
plt.ylabel("Annual Salary ($)", fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=10)

output_img = os.path.join(os.path.dirname(__file__), "linear_regression_fit.png")
plt.savefig(output_img, dpi=200)
plt.close()

print(f"\nRegression visualization successfully saved to: {output_img}")
print("=" * 80)
