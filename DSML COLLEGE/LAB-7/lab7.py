# ============================================================
# LAB 7: Linear Regression vs. Logistic Regression
# Dataset Used: Kaggle Red Wine Quality Dataset (winequality-red.csv)
# ============================================================
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix

# 1. Load Dataset
data_path = os.path.join(os.path.dirname(__file__), "dataset", "winequality-red.csv")
if not os.path.exists(data_path):
    data_path = "dataset/winequality-red.csv"

# Automatically detect delimiter (; or ,)
with open(data_path, "r") as f:
    sep = ";" if ";" in f.readline() else ","
df = pd.read_csv(data_path, sep=sep)
print(f"1. Dataset Loaded: {df.shape[0]} samples, {df.shape[1]} features")

# 2. Define Features and Targets
X = df.drop("quality", axis=1)
y_continuous = df["quality"]                   # Continuous rating (3.0 to 8.0)
y_binary = (df["quality"] >= 6).astype(int)     # Binary class (1 = High Quality, 0 = Low/Avg)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/Test Split (80% Train, 20% Test)
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X_scaled, y_continuous, test_size=0.2, random_state=42)
_, _, y_train_clf, y_test_clf = train_test_split(X_scaled, y_binary, test_size=0.2, random_state=42)

# ============================================================
# PART A: Linear Regression (Continuous Target)
# ============================================================
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train_reg)
y_pred_reg = lin_reg.predict(X_test)

print("\n2. Linear Regression (Predicting Continuous Wine Quality):")
print(f"   Mean Squared Error (MSE): {mean_squared_error(y_test_reg, y_pred_reg):.4f}")
print(f"   Sample Predictions:       {np.round(y_pred_reg[:5], 2)}")

# ============================================================
# PART B: Logistic Regression (Binary Classification)
# ============================================================
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train_clf)
y_pred_clf = log_reg.predict(X_test)

print("\n3. Logistic Regression (Classifying High vs. Low Quality):")
print(f"   Classification Accuracy:  {accuracy_score(y_test_clf, y_pred_clf) * 100:.2f}%")
print("   Confusion Matrix:")
print(confusion_matrix(y_test_clf, y_pred_clf))

# ============================================================
# Failure Mode: Linear Regression on Classification
# ============================================================
lin_clf = LinearRegression().fit(X_train, y_train_clf)
lin_preds = lin_clf.predict(X_test)
out_of_bounds = np.sum((lin_preds < 0) | (lin_preds > 1))

print("\n4. Why Linear Regression Fails on Classification:")
print(f"   Predictions outside valid probability [0, 1]: {out_of_bounds} / {len(X_test)}")
print("   Conclusion: Linear Regression outputs values < 0 or > 1, violating probability rules.")
print("               Logistic Regression squashes outputs to (0, 1) using the Sigmoid function.")
