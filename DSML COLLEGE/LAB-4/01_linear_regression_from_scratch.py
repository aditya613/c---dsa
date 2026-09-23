"""
LAB 4 - Step 1: Simple Linear Regression From Scratch (Ordinary Least Squares - OLS)
Topics Covered:
1. Formulation of Simple Linear Regression: y = beta_0 + beta_1 * x.
2. Derivation and implementation of closed-form OLS analytical equations:
   - Slope (beta_1) = sum((x_i - x_mean) * (y_i - y_mean)) / sum((x_i - x_mean)^2)
   - Intercept (beta_0) = y_mean - beta_1 * x_mean
3. Pure Python / NumPy vector implementation without external ML frameworks.
4. Calculation of core regression evaluation metrics:
   - Mean Squared Error (MSE)
   - Root Mean Squared Error (RMSE)
   - Mean Absolute Error (MAE)
   - Coefficient of Determination (R-squared score)
"""

import os
import numpy as np
import pandas as pd

print("=" * 80)
print("LAB 4 - PART 1: SIMPLE LINEAR REGRESSION FROM SCRATCH (OLS)")
print("=" * 80)

# 1. Load Dataset
dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "experience_salary.csv")
df = pd.read_csv(dataset_path)

x = df["Years_Experience"].values
y = df["Salary"].values
n = len(x)

print(f"Loaded {n} samples (Years_Experience -> Salary)")
print(df.head(5))

# 2. Compute Means
x_mean = np.mean(x)
y_mean = np.mean(y)
print(f"\nMean Experience (x_mean): {x_mean:.2f} years")
print(f"Mean Salary (y_mean):     ${y_mean:.2f}")

# 3. Calculate OLS Coefficients (Slope beta_1 and Intercept beta_0)
# beta_1 = Cov(x, y) / Var(x)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

beta_1 = numerator / denominator
beta_0 = y_mean - (beta_1 * x_mean)

print("\n--- Learned Regression Parameters (OLS Analytical Solution) ---")
print(f"Slope (beta_1 / Weight):    {beta_1:.4f}")
print(f"Intercept (beta_0 / Bias):  ${beta_0:.4f}")
print(f"Fitted Equation: Salary = {beta_0:.2f} + {beta_1:.2f} * (Years_Experience)")

# 4. Generate Predictions
y_pred = beta_0 + beta_1 * x

# 5. Compute Evaluation Metrics From Scratch
residuals = y - y_pred
mae = np.mean(np.abs(residuals))
mse = np.mean(residuals ** 2)
rmse = np.sqrt(mse)

ss_tot = np.sum((y - y_mean) ** 2)  # Total sum of squares
ss_res = np.sum(residuals ** 2)      # Residual sum of squares
r2_score = 1 - (ss_res / ss_tot)

print("\n--- Model Evaluation Metrics (From Scratch) ---")
print(f"Mean Absolute Error (MAE):       ${mae:.2f}")
print(f"Mean Squared Error (MSE):        {mse:.2f}")
print(f"Root Mean Squared Error (RMSE):  ${rmse:.2f}")
print(f"R-squared Score (R^2):           {r2_score:.4f} ({r2_score*100:.2f}% variance explained)")

# 6. Sample Predictions on New Unseen Experience Values
print("\n--- Making Real-World Inference ---")
test_experiences = [0.5, 3.5, 7.0, 12.0]
for exp in test_experiences:
    predicted_sal = beta_0 + beta_1 * exp
    print(f"Experience: {exp:4.1f} years -> Predicted Salary: ${predicted_sal:9.2f}")
print("=" * 80)
