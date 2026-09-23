"""
LAB 5 - Step 1: Single-Layer Perceptron Failure on Binary XOR
Historical Context:
In 1969, Marvin Minsky and Seymour Papert published 'Perceptrons', proving that
a single-layer perceptron cannot learn non-linearly separable functions like XOR.
This triggered the first 'AI Winter'.

Truth Table for XOR:
Input (x1, x2) -> Target (y)
(0, 0)          -> 0
(0, 1)          -> 1
(1, 0)          -> 1
(1, 1)          -> 0

In this script:
We attempt to train a single-layer perceptron (linear decision boundary) on XOR.
We observe that accuracy fails to reach 100% and oscillates between 50% and 75%.
"""

import numpy as np

print("=" * 80)
print("LAB 5 - PART 1: SINGLE-LAYER PERCEPTRON FAILURE ON XOR")
print("=" * 80)

# XOR Dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=float)

y = np.array([0, 1, 1, 0], dtype=float).reshape(-1, 1)

# Sigmoid Activation
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -250, 250)))

# Initialize weights and bias for a single linear perceptron
np.random.seed(42)
W = np.random.randn(2, 1)
b = 0.0
learning_rate = 0.5
epochs = 1000

print("Attempting to train Single-Layer Perceptron (2 inputs -> 1 output) on XOR...")

for epoch in range(epochs):
    # Forward pass: z = X*W + b, y_hat = sigmoid(z)
    z = np.dot(X, W) + b
    y_hat = sigmoid(z)
    
    # Binary Cross-Entropy Loss
    loss = -np.mean(y * np.log(y_hat + 1e-9) + (1 - y) * np.log(1 - y_hat + 1e-9))
    
    # Gradients
    dz = y_hat - y
    dW = np.dot(X.T, dz) / len(X)
    db = np.sum(dz) / len(X)
    
    # Updates
    W -= learning_rate * dW
    b -= learning_rate * db
    
    if (epoch + 1) % 200 == 0:
        predictions = (y_hat >= 0.5).astype(int)
        acc = np.mean(predictions == y) * 100
        print(f"Epoch {epoch + 1:4d} | Loss: {loss:.4f} | Accuracy: {acc:.1f}%")

# Final Predictions
final_pred = sigmoid(np.dot(X, W) + b)
print("\n--- Final Single-Layer Perceptron Predictions ---")
print("Input (x1, x2) | Actual | Predicted Prob | Binary Class")
print("-" * 55)
for (x1, x2), actual, prob in zip(X, y.flatten(), final_pred.flatten()):
    cls = int(prob >= 0.5)
    print(f"    ({int(x1)}, {int(x2)})      |   {int(actual)}    |     {prob:6.4f}     |      {cls}")

print("\nCONCLUSION: A single-layer perceptron CANNOT separate XOR because XOR is non-linearly separable.")
print("A hidden layer with non-linear activation (Multilayer Perceptron) is required!")
print("=" * 80)
