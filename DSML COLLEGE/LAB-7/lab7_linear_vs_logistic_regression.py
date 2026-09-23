"""
====================================================================================================
LAB 7: LINEAR REGRESSION VS. LOGISTIC REGRESSION COMPARISON
====================================================================================================
Objectives:
1. Implement Linear Regression and Logistic Regression using Scikit-Learn libraries.
2. Apply both models to the EXACT SAME Kaggle dataset (Red Wine Quality, 1,599 samples).
3. Compare model mechanics, mathematical formulations, and evaluation metrics based on problem
   type (Regression vs. Classification).
4. Demonstrate why Linear Regression is fundamentally ill-suited for classification tasks.
====================================================================================================
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    mean_squared_error,
    root_mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    roc_curve
)

# --------------------------------------------------------------------------------------------------
# STEP 1: LOAD & INSPECT THE KAGGLE DATASET
# --------------------------------------------------------------------------------------------------
print("=" * 85)
print("STEP 1: LOADING & INSPECTING KAGGLE RED WINE QUALITY DATASET")
print("=" * 85)

script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, "dataset", "winequality-red.csv")

# Detect separator automatically
with open(dataset_path, "r") as f:
    first_line = f.readline()
sep = ";" if ";" in first_line else ","

df = pd.read_csv(dataset_path, sep=sep)

print(f"Dataset Successfully Loaded from: {dataset_path}")
print(f"Dataset Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print("\nFirst 5 Records:")
print(df.head())

print("\nMissing Values Count:")
print(df.isnull().sum())

# Feature matrix (11 physiochemical properties)
feature_names = [col for col in df.columns if col != "quality"]
X = df[feature_names]

# Target 1: Continuous wine quality score (ranging from 3 to 8)
y_continuous = df["quality"]

# Target 2: Binary wine quality classification (1: Good Quality >= 6, 0: Average/Poor Quality < 6)
# Thresholding quality at 6 is standard Kaggle benchmark for this dataset
y_binary = (df["quality"] >= 6).astype(int)

print(f"\nContinuous Target (Regression) Quality Distribution:")
print(y_continuous.describe())

print(f"\nBinary Target (Classification) Class Distribution:")
print(y_binary.value_counts(normalize=True).rename({0: "Class 0 (Quality < 6)", 1: "Class 1 (Quality >= 6)"}))

# --------------------------------------------------------------------------------------------------
# STEP 2: PROBLEM TYPE A - REGRESSION WITH LINEAR REGRESSION
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 2: PROBLEM TYPE A - CONTINUOUS TARGET PREDICTION (LINEAR REGRESSION)")
print("=" * 85)
print("Goal: Predict the continuous numeric quality score of wine (e.g. 5.62, 6.14).")

# Train/Test split for regression
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X, y_continuous, test_size=0.20, random_state=42
)

# Standardize features for stable coefficient estimation
scaler_reg = StandardScaler()
X_train_reg_scaled = scaler_reg.fit_transform(X_train_reg)
X_test_reg_scaled = scaler_reg.transform(X_test_reg)

# Train Linear Regression Model
lin_reg = LinearRegression()
lin_reg.fit(X_train_reg_scaled, y_train_reg)

# Predictions
y_pred_reg = lin_reg.predict(X_test_reg_scaled)

# Compute Regression Evaluation Metrics
mse = mean_squared_error(y_test_reg, y_pred_reg)
try:
    rmse = root_mean_squared_error(y_test_reg, y_pred_reg)
except AttributeError:
    rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"Linear Regression Intercept (beta_0): {lin_reg.intercept_:.4f}")
print("Top 3 Feature Weights (|coefficient|):")
coef_series = pd.Series(lin_reg.coef_, index=feature_names).sort_values(key=abs, ascending=False)
for feat, coef in coef_series.head(3).items():
    print(f"   -> {feat:22s}: {coef:+.4f}")

print("\n--- REGRESSION PERFORMANCE METRICS ---")
print(f"Mean Squared Error (MSE)         : {mse:.4f}")
print(f"Root Mean Squared Error (RMSE)   : {rmse:.4f}  (Average error in quality score points)")
print(f"Mean Absolute Error (MAE)        : {mae:.4f}")
print(f"R-squared Score (R^2)            : {r2:.4f}  (Explains {r2*100:.2f}% of wine quality variance)")

# --------------------------------------------------------------------------------------------------
# STEP 3: PROBLEM TYPE B - CLASSIFICATION WITH LOGISTIC REGRESSION
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 3: PROBLEM TYPE B - DISCRETE CLASS PREDICTION (LOGISTIC REGRESSION)")
print("=" * 85)
print("Goal: Classify whether a wine is High Quality (1) or Average/Low Quality (0).")

# Stratified Train/Test split for balanced class distribution
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X, y_binary, test_size=0.20, random_state=42, stratify=y_binary
)

# Standardize features (essential for regularized logistic regression convergence)
scaler_clf = StandardScaler()
X_train_clf_scaled = scaler_clf.fit_transform(X_train_clf)
X_test_clf_scaled = scaler_clf.transform(X_test_clf)

# Train Logistic Regression Model
log_reg = LogisticRegression(max_iter=1000, random_state=42)
log_reg.fit(X_train_clf_scaled, y_train_clf)

# Predictions: Discrete class predictions and Continuous predicted probabilities
y_pred_clf = log_reg.predict(X_test_clf_scaled)
y_pred_proba_clf = log_reg.predict_proba(X_test_clf_scaled)[:, 1]

# Compute Classification Evaluation Metrics
acc = accuracy_score(y_test_clf, y_pred_clf)
prec = precision_score(y_test_clf, y_pred_clf)
rec = recall_score(y_test_clf, y_pred_clf)
f1 = f1_score(y_test_clf, y_pred_clf)
roc_auc = roc_auc_score(y_test_clf, y_pred_proba_clf)
cm = confusion_matrix(y_test_clf, y_pred_clf)

print("\n--- CLASSIFICATION PERFORMANCE METRICS ---")
print(f"Accuracy Score                   : {acc:.4f}  ({acc*100:.2f}% correctly classified)")
print(f"Precision Score (Class 1)        : {prec:.4f}  (Ratio of correct good wine alerts)")
print(f"Recall / Sensitivity Score       : {rec:.4f}  (Coverage of all actual good wines)")
print(f"F1-Score (Harmonic Mean)         : {f1:.4f}")
print(f"Area Under ROC Curve (ROC-AUC)   : {roc_auc:.4f}")

print("\nConfusion Matrix:")
print("                 Predicted Class 0    Predicted Class 1")
print(f"Actual Class 0 :       {cm[0, 0]:4d} (TN)             {cm[0, 1]:4d} (FP)")
print(f"Actual Class 1 :       {cm[1, 0]:4d} (FN)             {cm[1, 1]:4d} (TP)")

print("\nClassification Report:")
print(classification_report(y_test_clf, y_pred_clf, target_names=["Low/Avg Quality (0)", "Good Quality (1)"]))

# --------------------------------------------------------------------------------------------------
# STEP 4: HEAD-TO-HEAD COMPARISON ON THE SAME DATASET
# --------------------------------------------------------------------------------------------------
print("=" * 85)
print("STEP 4: DIRECT HEAD-TO-HEAD COMPARISON (WHY NOT USE LINEAR REGRESSION FOR CLASSIFICATION?)")
print("=" * 85)

# Fit Linear Regression directly on the binary 0/1 labels to observe the failure mode
lin_clf = LinearRegression()
lin_clf.fit(X_train_clf_scaled, y_train_clf)
y_lin_continuous_preds = lin_clf.predict(X_test_clf_scaled)

# Convert linear regression continuous outputs to binary classes using threshold 0.5
y_lin_binary_preds = (y_lin_continuous_preds >= 0.5).astype(int)

lin_acc = accuracy_score(y_test_clf, y_lin_binary_preds)
lin_out_of_bounds = np.sum((y_lin_continuous_preds < 0) | (y_lin_continuous_preds > 1))

print(f"1. Unbounded Output Issue in Linear Regression:")
print(f"   - Min predicted linear value : {y_lin_continuous_preds.min():.4f}")
print(f"   - Max predicted linear value : {y_lin_continuous_preds.max():.4f}")
print(f"   - Number of predictions outside valid probability bounds [0, 1]: {lin_out_of_bounds} / {len(y_test_clf)}")
print(f"   -> Linear Regression outputs can be negative or > 1, violating probability rules!")

print(f"\n2. Bounded Sigmoid Output in Logistic Regression:")
print(f"   - Min predicted probability  : {y_pred_proba_clf.min():.4f}")
print(f"   - Max predicted probability  : {y_pred_proba_clf.max():.4f}")
print(f"   -> Logistic Regression is strictly constrained to (0, 1) by sigma(z) = 1 / (1 + e^-z).")

# Master Comparison Table
print("\n" + "=" * 85)
print(f"{'CRITERION / ATTRIBUTE':<32} | {'LINEAR REGRESSION':<25} | {'LOGISTIC REGRESSION':<25}")
print("-" * 85)
print(f"{'Problem Type':<32} | {'Regression (Continuous)':<25} | {'Classification (Discrete)':<25}")
print(f"{'Target Variable Y':<32} | {'Continuous scale [3.0 - 8.0]':<25} | {'Binary class {0, 1}':<25}")
print(f"{'Hypothesis Function':<32} | {'y_hat = theta^T * X':<25} | {'P(y=1) = sigma(theta^T * X)':<25}")
print(f"{'Output Range':<32} | {'(-infinity, +infinity)':<25} | {'(0, 1) calibrated probability':<25}")
print(f"{'Loss / Objective Function':<32} | {'Mean Squared Error (MSE)':<25} | {'Binary Cross-Entropy (Log-Loss)':<25}")
print(f"{'Parameter Estimation':<32} | {'Closed-form OLS / GD':<25} | {'Maximum Likelihood Estimation':<25}")
print(f"{'Sensitivity to Extreme Points':<32} | {'High (Residuals squared)':<25} | {'Robust (Sigmoid saturates)':<25}")
print(f"{'Key Performance Metrics':<32} | {'R^2, MSE, RMSE, MAE':<25} | {'Accuracy, F1, ROC-AUC, CM':<25}")
print("=" * 85)

# --------------------------------------------------------------------------------------------------
# STEP 5: VISUALIZATION & ARTIFACT GENERATION
# --------------------------------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle("Linear Regression vs. Logistic Regression (Kaggle Wine Quality Dataset)", fontsize=16, fontweight='bold')

# Panel 1: Linear Regression Actual vs. Predicted
ax1 = axes[0, 0]
ax1.scatter(y_test_reg, y_pred_reg, alpha=0.5, color='#1f77b4', edgecolors='k', s=45)
min_val = min(y_test_reg.min(), y_pred_reg.min())
max_val = max(y_test_reg.max(), y_pred_reg.max())
ax1.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label="Ideal Prediction (y = y_hat)")
ax1.set_title(f"Linear Regression: Actual vs. Predicted Quality\n(R^2 = {r2:.3f}, RMSE = {rmse:.3f})", fontsize=11, fontweight='bold')
ax1.set_xlabel("Actual Wine Quality")
ax1.set_ylabel("Predicted Wine Quality")
ax1.legend(loc="upper left")
ax1.grid(True, linestyle=":", alpha=0.6)

# Panel 2: Linear Regression Residual Plot
ax2 = axes[0, 1]
residuals = y_test_reg - y_pred_reg
ax2.scatter(y_pred_reg, residuals, alpha=0.5, color='#2ca02c', edgecolors='k', s=45)
ax2.axhline(0, color='r', linestyle='--', lw=2)
ax2.set_title(f"Linear Regression: Residuals vs. Fitted Values\n(Mean Absolute Error = {mae:.3f})", fontsize=11, fontweight='bold')
ax2.set_xlabel("Fitted Values (Predicted Quality)")
ax2.set_ylabel("Residual Error (Actual - Predicted)")
ax2.grid(True, linestyle=":", alpha=0.6)

# Panel 3: Logistic Regression Confusion Matrix Heatmap
ax3 = axes[1, 0]
cax = ax3.matshow(cm, cmap='Blues', alpha=0.8)
fig.colorbar(cax, ax=ax3, fraction=0.046, pad=0.04)
for i in range(2):
    for j in range(2):
        ax3.text(j, i, str(cm[i, j]), ha='center', va='center', fontsize=14, fontweight='bold',
                 color='white' if cm[i, j] > cm.max()/2 else 'black')
ax3.set_xticks([0, 1])
ax3.set_yticks([0, 1])
ax3.set_xticklabels(["Pred 0 (Avg)", "Pred 1 (Good)"], fontsize=10)
ax3.set_yticklabels(["Actual 0 (Avg)", "Actual 1 (Good)"], fontsize=10)
ax3.set_title(f"Logistic Regression: Confusion Matrix\n(Accuracy = {acc:.3f}, F1-Score = {f1:.3f})", fontsize=11, fontweight='bold')

# Panel 4: Logistic Regression ROC Curve
ax4 = axes[1, 1]
fpr, tpr, _ = roc_curve(y_test_clf, y_pred_proba_clf)
ax4.plot(fpr, tpr, color='#ff7f0e', lw=2.5, label=f"Logistic Regression ROC (AUC = {roc_auc:.3f})")
ax4.plot([0, 1], [0, 1], color='navy', linestyle='--', lw=1.5, label="Random Guess Baseline (AUC = 0.50)")
ax4.set_title(f"Logistic Regression: ROC Curve Analysis", fontsize=11, fontweight='bold')
ax4.set_xlabel("False Positive Rate (1 - Specificity)")
ax4.set_ylabel("True Positive Rate (Recall / Sensitivity)")
ax4.legend(loc="lower right")
ax4.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
output_fig = os.path.join(script_dir, "linear_vs_logistic_comparison.png")
plt.savefig(output_fig, dpi=300, bbox_inches='tight')
plt.close()

print(f"\nMulti-panel comparison chart saved successfully to:\n -> {output_fig}")
print("=" * 85)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("=" * 85)
