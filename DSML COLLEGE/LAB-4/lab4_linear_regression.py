# LAB 4: Simple Linear Regression (Salary Prediction)
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Dataset
path = os.path.join(os.path.dirname(__file__), "dataset", "experience_salary.csv")
df = pd.read_csv(path)

X = df[["Years_Experience"]]
y = df["Salary"]

# 2. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Fit Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict
y_pred = model.predict(X_test)

# 5. Evaluate Metrics
print("--- Linear Regression Results ---")
print(f"Slope (w):               {model.coef_[0]:.2f}")
print(f"Intercept (b):           {model.intercept_:.2f}")
print(f"Mean Squared Error (MSE):{mean_squared_error(y_test, y_pred):.2f}")
print(f"R-squared (R2 Score):    {r2_score(y_test, y_pred):.2f}")

# 6. Plot Fit Line
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary Fit")
plt.legend()
plt.savefig("linear_regression_fit.png")
print("Saved plot to 'linear_regression_fit.png'")
