"""
====================================================================================================
LAB 4: SIMPLE LINEAR REGRESSION (OLS ANALYTICAL, GRADIENT DESCENT & SCIKIT-LEARN)
====================================================================================================
Objectives:
1. Master theoretical and mathematical derivation of Simple Linear Regression.
2. Implement closed-form Ordinary Least Squares (OLS) from scratch.
3. Implement iterative Batch Gradient Descent optimization from scratch.
4. Implement model training using Scikit-Learn (LinearRegression).
5. Evaluate predictive accuracy using standard metrics: R^2, MSE, RMSE, MAE.
6. Visualize fitted regression line, data scatter points, and residual error bars.
====================================================================================================
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# --------------------------------------------------------------------------------------------------
# STEP 1: LOAD REALISTIC KAGGLE SALARY & EXPERIENCE DATASET
# --------------------------------------------------------------------------------------------------
print("=" * 85)
print("STEP 1: LOADING KAGGLE SALARY & EXPERIENCE DATASET (500 SAMPLES)")
print("=" * 85)

script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, "dataset", "salary_kaggle.csv")

df = pd.read_csv(dataset_path)
print(f"Dataset Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print("\nFirst 5 Records:")
print(df.head())

X_raw = df["YearsExperience"].values
y_raw = df["Salary"].values

# Train/Test Split (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X_raw, y_raw, test_size=0.20, random_state=42)
print(f"Training Samples: {len(X_train)} | Testing Samples: {len(X_test)}")

# --------------------------------------------------------------------------------------------------
# STEP 2: METHOD 1 - CLOSED-FORM ORDINARY LEAST SQUARES (OLS) FROM SCRATCH
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 2: METHOD 1 - CLOSED-FORM ORDINARY LEAST SQUARES (OLS)")
print("=" * 85)

# Analytical formulas:
# beta_1 = Cov(X, Y) / Var(X) = sum((X - x_bar) * (Y - y_bar)) / sum((X - x_bar)^2)
# beta_0 = y_bar - beta_1 * x_bar
x_bar = np.mean(X_train)
y_bar = np.mean(y_train)

numerator = np.sum((X_train - x_bar) * (y_train - y_bar))
denominator = np.sum((X_train - x_bar) ** 2)

beta_1_ols = numerator / denominator
beta_0_ols = y_bar - (beta_1_ols * x_bar)

print(f"OLS Analytical Slope (beta_1 / Weight)     : {beta_1_ols:.4f}")
print(f"OLS Analytical Intercept (beta_0 / Bias)   : {beta_0_ols:.4f}")
print(f"Derived Model Equation: Salary = {beta_0_ols:.2f} + {beta_1_ols:.2f} * (YearsExperience)")

# --------------------------------------------------------------------------------------------------
# STEP 3: METHOD 2 - ITERATIVE BATCH GRADIENT DESCENT FROM SCRATCH
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 3: METHOD 2 - BATCH GRADIENT DESCENT OPTIMIZATION")
print("=" * 85)

# Feature standardization for stable gradient descent convergence
x_mean_gd, x_std_gd = np.mean(X_train), np.std(X_train)
X_train_gd_scaled = (X_train - x_mean_gd) / x_std_gd

theta_0 = 0.0
theta_1 = 0.0
alpha = 0.01          # Learning rate
epochs = 1500         # Optimization iterations
m = len(X_train)
cost_history = []

for epoch in range(epochs):
    # Hypothesis: y_hat = theta_0 + theta_1 * x
    y_hat = theta_0 + theta_1 * X_train_gd_scaled
    error = y_hat - y_train
    
    # Cost function: J = 1/(2m) * sum(error^2)
    cost = (1 / (2 * m)) * np.sum(error ** 2)
    cost_history.append(cost)
    
    # Gradients
    d_theta_0 = (1 / m) * np.sum(error)
    d_theta_1 = (1 / m) * np.sum(error * X_train_gd_scaled)
    
    # Simultaneous parameter update
    theta_0 -= alpha * d_theta_0
    theta_1 -= alpha * d_theta_1

# Unscale parameters back to original domain
beta_1_gd = theta_1 / x_std_gd
beta_0_gd = theta_0 - (theta_1 * x_mean_gd / x_std_gd)

print(f"Gradient Descent Slope (beta_1)            : {beta_1_gd:.4f}")
print(f"Gradient Descent Intercept (beta_0)        : {beta_0_gd:.4f}")
print(f"Initial Cost: {cost_history[0]:,.2f} -> Final Cost: {cost_history[-1]:,.2f} (Converged!)")

# --------------------------------------------------------------------------------------------------
# STEP 4: METHOD 3 - SCIKIT-LEARN LINEAR REGRESSION
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 4: METHOD 3 - SCIKIT-LEARN LINEAR REGRESSION & EVALUATION METRICS")
print("=" * 85)

model = LinearRegression()
model.fit(X_train.reshape(-1, 1), y_train)

beta_1_sklearn = model.coef_[0]
beta_0_sklearn = model.intercept_

print(f"Scikit-Learn Slope (coef_)                 : {beta_1_sklearn:.4f}")
print(f"Scikit-Learn Intercept (intercept_)        : {beta_0_sklearn:.4f}")

# Cross-Verification of Parameters
print("\n--- PARAMETER COMPARISON ACROSS ALL 3 IMPLEMENTATIONS ---")
print(f"{'Method':<25} | {'Slope (beta_1)':<18} | {'Intercept (beta_0)':<18}")
print("-" * 65)
print(f"{'OLS Analytical Scratch':<25} | {beta_1_ols:<18.4f} | {beta_0_ols:<18.4f}")
print(f"{'Gradient Descent Scratch':<25} | {beta_1_gd:<18.4f} | {beta_0_gd:<18.4f}")
print(f"{'Scikit-Learn Model':<25} | {beta_1_sklearn:<18.4f} | {beta_0_sklearn:<18.4f}")

# Evaluate on Unseen Test Data
y_pred = model.predict(X_test.reshape(-1, 1))

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- MODEL PERFORMANCE METRICS ON UNSEEN TEST SET ---")
print(f"Mean Squared Error (MSE)         : {mse:,.2f}")
print(f"Root Mean Squared Error (RMSE)   : ${rmse:,.2f} (Typical error in salary dollars)")
print(f"Mean Absolute Error (MAE)        : ${mae:,.2f}")
print(f"R-squared Score (R^2)            : {r2:.4f} ({r2*100:.2f}% of salary variance explained)")

# --------------------------------------------------------------------------------------------------
# STEP 5: VISUALIZATION OF FITTED LINE & RESIDUAL ERRORS
# --------------------------------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Linear Regression Modeling (Kaggle Salary Dataset)", fontsize=15, fontweight='bold')

# Panel 1: Regression Fit with Residual Error Bars
ax1 = axes[0]
ax1.scatter(X_test, y_test, color='#1f77b4', alpha=0.7, edgecolors='k', s=50, label='Actual Test Data')
x_line = np.linspace(X_raw.min(), X_raw.max(), 200)
y_line = model.predict(x_line.reshape(-1, 1))
ax1.plot(x_line, y_line, color='red', lw=2.5, label=f'Fit: y = {beta_0_sklearn:.0f} + {beta_1_sklearn:.0f}x')

# Draw residual error lines for a sample of points
sample_indices = np.random.choice(len(X_test), 25, replace=False)
for idx in sample_indices:
    ax1.plot([X_test[idx], X_test[idx]], [y_test[idx], y_pred[idx]], color='gray', linestyle=':', lw=1.2)

ax1.set_title(f"Fitted Regression Line & Residual Errors\n(R^2 = {r2:.3f}, RMSE = ${rmse:,.0f})", fontweight='bold')
ax1.set_xlabel("Years of Experience")
ax1.set_ylabel("Annual Salary ($)")
ax1.legend()
ax1.grid(True, linestyle=":", alpha=0.6)

# Panel 2: Gradient Descent Cost Convergence Curve
ax2 = axes[1]
ax2.plot(cost_history, color='#2ca02c', lw=2)
ax2.set_title("Gradient Descent Optimization: Loss Function J(theta)", fontweight='bold')
ax2.set_xlabel("Epochs")
ax2.set_ylabel("Mean Squared Error Cost J")
ax2.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
out_plot = os.path.join(script_dir, "linear_regression_fit.png")
plt.savefig(out_plot, dpi=300)
plt.close()

print(f"\nVisualization saved to:\n -> {out_plot}")
print("=" * 85)
print("LAB 4 COMPLETED SUCCESSFULLY!")
print("=" * 85)
