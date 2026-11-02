# Lab 4 - Part 1: Linear Regression from Scratch (OLS Analytical Formula)
import os
import numpy as np
import pandas as pd

# 1. Load data
path = os.path.join(os.path.dirname(__file__), "dataset", "experience_salary.csv")
df = pd.read_csv(path)
x = df["Years_Experience"].values
y = df["Salary"].values

# 2. Compute means
x_mean = np.mean(x)
y_mean = np.mean(y)

# 3. Calculate Slope (beta_1) and Intercept (beta_0)
# beta_1 = Cov(X, Y) / Var(X)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

beta_1 = numerator / denominator
beta_0 = y_mean - (beta_1 * x_mean)

print(f"Slope (beta_1):     {beta_1:.2f}")
print(f"Intercept (beta_0): {beta_0:.2f}")
print(f"Model Equation: Salary = {beta_0:.2f} + {beta_1:.2f} * Experience")

# 4. Predict for 5 years experience
pred = beta_0 + beta_1 * 5
print(f"Predicted Salary for 5 Years Experience: ${pred:,.2f}")
