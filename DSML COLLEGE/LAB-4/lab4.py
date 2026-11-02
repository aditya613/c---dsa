# ============================================================
# LAB 4: Simple Linear Regression (OLS & Scikit-Learn)
# Dataset Used: Experience vs Salary Dataset (experience_salary.csv)
# ============================================================
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Dataset
data_path = os.path.join(os.path.dirname(__file__), "dataset", "experience_salary.csv")
if not os.path.exists(data_path):
    data_path = "dataset/experience_salary.csv"
df = pd.read_csv(data_path)

print(f"1. Dataset Loaded: {df.shape[0]} samples")
print(df.head(3))

X = df[["Years_Experience"]]
y = df["Salary"]

# 2. Mathematical OLS from Scratch (Analytical Solution)
# beta_1 = Cov(X, Y) / Var(X),  beta_0 = mean(y) - beta_1 * mean(x)
x_arr = df["Years_Experience"].values
y_arr = df["Salary"].values
beta_1 = np.sum((x_arr - x_arr.mean()) * (y_arr - y_arr.mean())) / np.sum((x_arr - x_arr.mean()) ** 2)
beta_0 = y_arr.mean() - beta_1 * x_arr.mean()

print("\n2. Ordinary Least Squares (From Scratch Analytical Solution):")
print(f"   Calculated Slope (beta_1):     {beta_1:.2f}")
print(f"   Calculated Intercept (beta_0): {beta_0:.2f}")

# 3. Scikit-Learn Implementation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predictions and Evaluation Metrics
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n3. Scikit-Learn Linear Regression Results:")
print(f"   Model Slope (w):          {model.coef_[0]:.2f}")
print(f"   Model Intercept (b):      {model.intercept_:.2f}")
print(f"   Mean Squared Error (MSE): {mse:.2f}")
print(f"   R-squared (R2 Score):     {r2:.2f} ({r2 * 100:.1f}% variance explained)")

# 5. Predict New Value
new_exp = [[5.0]]
predicted_salary = model.predict(new_exp)[0]
print(f"\n4. Prediction: Salary for 5 Years Experience: ${predicted_salary:,.2f}")
