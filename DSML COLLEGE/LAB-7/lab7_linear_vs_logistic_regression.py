# LAB 7: Linear Regression vs. Logistic Regression (Wine Quality Dataset)
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix

# 1. Load Dataset
path = os.path.join(os.path.dirname(__file__), "dataset", "winequality-red.csv")
with open(path, "r") as f:
    sep = ";" if ";" in f.readline() else ","
df = pd.read_csv(path, sep=sep)

X = df.drop("quality", axis=1)
y_continuous = df["quality"]                   # For Regression: continuous score (3 to 8)
y_binary = (df["quality"] >= 6).astype(int)     # For Classification: 1 if Good (>= 6), else 0

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/Test Split
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X_scaled, y_continuous, test_size=0.2, random_state=42)
_, _, y_train_clf, y_test_clf = train_test_split(X_scaled, y_binary, test_size=0.2, random_state=42)

# ==========================================
# PART A: Linear Regression (Continuous Target)
# ==========================================
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train_reg)
y_pred_reg = lin_reg.predict(X_test)

print("=== 1. LINEAR REGRESSION (Predicting Exact Quality) ===")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test_reg, y_pred_reg):.4f}")
print(f"Sample Predictions:       {np.round(y_pred_reg[:5], 2)}")

# ==========================================
# PART B: Logistic Regression (Binary Classification)
# ==========================================
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train_clf)
y_pred_clf = log_reg.predict(X_test)

print("\n=== 2. LOGISTIC REGRESSION (Classifying High vs Low Quality) ===")
print(f"Classification Accuracy:  {accuracy_score(y_test_clf, y_pred_clf) * 100:.2f}%")
print("Confusion Matrix:\n", confusion_matrix(y_test_clf, y_pred_clf))

# ==========================================
# Failure of Linear Regression for Classification
# ==========================================
lin_on_binary = LinearRegression().fit(X_train, y_train_clf)
lin_preds = lin_on_binary.predict(X_test)
out_of_bounds = np.sum((lin_preds < 0) | (lin_preds > 1))
print(f"\n[!] Linear Regression Predictions outside valid probability [0, 1]: {out_of_bounds}")
print("Conclusion: Linear Regression produces unbounded predictions (<0 or >1), making Logistic Regression the right tool for classification.")
