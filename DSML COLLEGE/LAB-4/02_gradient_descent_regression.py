"""
LAB 4 - Step 2: Linear Regression Optimized via Batch Gradient Descent
Topics Covered:
1. Optimization perspective of Linear Regression.
2. Mean Squared Error (MSE) Cost Function: J(theta_0, theta_1) = (1 / 2n) * sum((y_hat_i - y_i)^2).
3. Computing analytical partial gradients:
   - dJ / d(theta_0) = (1 / n) * sum(y_hat_i - y_i)
   - dJ / d(theta_1) = (1 / n) * sum((y_hat_i - y_i) * x_i)
4. Parameter update rule with learning rate (alpha).
5. Tracking loss per epoch and plotting convergence curve.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 80)
print("LAB 4 - PART 2: LINEAR REGRESSION VIA GRADIENT DESCENT")
print("=" * 80)

dataset_path = os.path.join(os.path.dirname(__file__), "dataset", "experience_salary.csv")
df = pd.read_csv(dataset_path)

x_raw = df["Years_Experience"].values
y_raw = df["Salary"].values
n = len(x_raw)

# Feature normalization for stable and fast gradient descent convergence
x_mean, x_std = x_raw.mean(), x_raw.std()
x_scaled = (x_raw - x_mean) / x_std

# Hyperparameters
learning_rate = 0.05
epochs = 500

# Initialize parameters (theta_0 = bias, theta_1 = weight)
theta_0 = 0.0
theta_1 = 0.0

cost_history = []

print(f"Dataset Size: {n} samples")
print(f"Hyperparameters -> Learning Rate: {learning_rate}, Epochs: {epochs}")
print("\n--- Training Loop ---")

for epoch in range(epochs):
    # Forward pass (predictions)
    y_pred = theta_0 + (theta_1 * x_scaled)
    
    # Error residuals
    error = y_pred - y_raw
    
    # Compute MSE cost: J = (1 / (2*n)) * sum(error^2)
    cost = (1 / (2 * n)) * np.sum(error ** 2)
    cost_history.append(cost)
    
    # Compute gradients
    grad_theta_0 = (1 / n) * np.sum(error)
    grad_theta_1 = (1 / n) * np.sum(error * x_scaled)
    
    # Gradient descent update
    theta_0 -= learning_rate * grad_theta_0
    theta_1 -= learning_rate * grad_theta_1
    
    if (epoch + 1) % 100 == 0 or epoch == 0:
        print(f"Epoch {epoch + 1:3d}/{epochs} -> Cost (MSE/2): {cost:12.2f} | theta_0: ${theta_0:9.2f}, theta_1: ${theta_1:9.2f}")

# Convert scaled parameters back to original unscaled feature space
# y = theta_0 + theta_1 * ((x - x_mean) / x_std)
#   = (theta_0 - (theta_1 * x_mean / x_std)) + (theta_1 / x_std) * x
unscaled_slope = theta_1 / x_std
unscaled_intercept = theta_0 - (theta_1 * x_mean / x_std)

print("\n--- Gradient Descent Converged Parameters ---")
print(f"Unscaled Slope (beta_1):     {unscaled_slope:.4f}")
print(f"Unscaled Intercept (beta_0): ${unscaled_intercept:.4f}")

# Plot Loss Convergence Curve
plt.figure(figsize=(9, 5))
plt.plot(range(1, epochs + 1), cost_history, color='#2563eb', linewidth=2.5)
plt.title("Gradient Descent Cost Function J(theta) Convergence Curve", fontsize=12, fontweight='bold')
plt.xlabel("Iteration / Epoch", fontsize=10)
plt.ylabel("Cost Value (MSE / 2)", fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

output_img = os.path.join(os.path.dirname(__file__), "gradient_descent_convergence.png")
plt.savefig(output_img, dpi=200)
plt.close()
print(f"Convergence plot successfully saved to: {output_img}")
print("=" * 80)
