# Lab 4 - Part 2: Linear Regression using Gradient Descent
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)
n = len(x)

# Initialize parameters
w = 0.0  # weight (slope)
b = 0.0  # bias (intercept)
learning_rate = 0.01
epochs = 1000

# Gradient Descent Loop
for epoch in range(epochs):
    y_pred = w * x + b
    error = y_pred - y
    
    # Compute gradients
    dw = (2 / n) * np.sum(error * x)
    db = (2 / n) * np.sum(error)
    
    # Update parameters
    w -= learning_rate * dw
    b -= learning_rate * db

print("--- Gradient Descent Results ---")
print(f"Trained Weight (Slope):    {w:.2f}")
print(f"Trained Bias (Intercept):  {b:.2f}")
print(f"Prediction for x = 6:      {w * 6 + b:.2f}")
