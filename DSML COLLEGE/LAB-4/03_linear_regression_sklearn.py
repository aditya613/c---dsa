# Lab 4 - Part 3: Linear Regression with Scikit-Learn
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load data
path = os.path.join(os.path.dirname(__file__), "dataset", "experience_salary.csv")
df = pd.read_csv(path)

X = df[["Years_Experience"]]
y = df["Salary"]

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict and Evaluate
y_pred = model.predict(X_test)
print(f"Slope (Coefficient): {model.coef_[0]:.2f}")
print(f"Intercept:           {model.intercept_:.2f}")
print(f"Mean Squared Error:  {mean_squared_error(y_test, y_pred):.2f}")
print(f"R-squared Score:     {r2_score(y_test, y_pred):.2f}")
