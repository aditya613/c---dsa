"""
LAB 5 - Step 2: Multilayer Perceptron (MLP) for XOR From Scratch (NumPy)
Architecture:
- Input Layer: 2 neurons (x1, x2)
- Hidden Layer: 2 neurons with Sigmoid non-linear activation
- Output Layer: 1 neuron with Sigmoid activation

Derivation of Backpropagation (Chain Rule):
Let BCE Loss: L = -[y*log(A2) + (1-y)*log(1-A2)]
1. Output Layer:
   dZ2 = dL/dZ2 = (A2 - y)
   dW2 = (A1^T * dZ2) / m
   db2 = sum(dZ2) / m
2. Hidden Layer:
   dA1 = dZ2 * W2^T
   dZ1 = dA1 * sigma'(Z1) = dA1 * (A1 * (1 - A1))
   dW1 = (X^T * dZ1) / m
   db1 = sum(dZ1) / m
"""

import numpy as np

print("=" * 80)
print("LAB 5 - PART 2: MULTILAYER PERCEPTRON (2-2-1) FOR XOR FROM SCRATCH")
print("=" * 80)

# XOR Dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=float)

y = np.array([[0], [1], [1], [0]], dtype=float)
m = len(X)

# Activation functions
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -250, 250)))

def sigmoid_derivative(a):
    return a * (1.0 - a)

# Initialize Network Weights and Biases (Seed for reproducibility)
np.random.seed(42)
input_dim = 2
hidden_dim = 2
output_dim = 1

# He / Xavier style initialization
W1 = np.random.uniform(-1.0, 1.0, (input_dim, hidden_dim))
b1 = np.zeros((1, hidden_dim))

W2 = np.random.uniform(-1.0, 1.0, (hidden_dim, output_dim))
b2 = np.zeros((1, output_dim))

learning_rate = 1.0
epochs = 5000

print(f"Network Architecture: [{input_dim} Inputs] -> [{hidden_dim} Hidden Neurons (Sigmoid)] -> [{output_dim} Output Neuron (Sigmoid)]")
print(f"Hyperparameters -> Learning Rate: {learning_rate}, Epochs: {epochs}\n")

# Training Loop
for epoch in range(epochs):
    # ------------------
    # 1. FORWARD PASS
    # ------------------
    Z1 = np.dot(X, W1) + b1          # Hidden pre-activation: (4, 2)
    A1 = sigmoid(Z1)                 # Hidden activation: (4, 2)
    
    Z2 = np.dot(A1, W2) + b2         # Output pre-activation: (4, 1)
    A2 = sigmoid(Z2)                 # Output activation (y_hat): (4, 1)
    
    # Binary Cross-Entropy Loss
    loss = -np.mean(y * np.log(A2 + 1e-9) + (1.0 - y) * np.log(1.0 - A2 + 1e-9))
    
    # ------------------
    # 2. BACKPROPAGATION
    # ------------------
    # Output Layer Gradients
    dZ2 = A2 - y                     # Derivative of BCE with Sigmoid: (4, 1)
    dW2 = np.dot(A1.T, dZ2) / m      # (2, 1)
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m  # (1, 1)
    
    # Hidden Layer Gradients (Chain Rule)
    dA1 = np.dot(dZ2, W2.T)          # (4, 2)
    dZ1 = dA1 * sigmoid_derivative(A1)  # Element-wise product: (4, 2)
    dW1 = np.dot(X.T, dZ1) / m       # (2, 2)
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m  # (1, 2)
    
    # ------------------
    # 3. WEIGHT UPDATES (Gradient Descent)
    # ------------------
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    
    if (epoch + 1) % 1000 == 0 or epoch == 0:
        predictions = (A2 >= 0.5).astype(int)
        acc = np.mean(predictions == y) * 100
        print(f"Epoch {epoch + 1:4d}/{epochs} | BCE Loss: {loss:.5f} | Accuracy: {acc:.1f}%")

# ------------------
# 4. FINAL VERIFICATION
# ------------------
print("\n" + "=" * 60)
print("FINAL MLP EVALUATION ON XOR TRUTH TABLE")
print("=" * 60)
print("Input (x1, x2) | Expected | Raw Network Prob | Predicted Class | Status")
print("-" * 65)

for (x1, x2), actual, prob in zip(X, y.flatten(), A2.flatten()):
    pred_cls = int(prob >= 0.5)
    status = "SUCCESS [CORRECT]" if pred_cls == int(actual) else "FAIL [WRONG]"
    print(f"    ({int(x1)}, {int(x2)})      |    {int(actual)}     |      {prob:7.5f}     |        {pred_cls}        | {status}")

print("-" * 65)
print("Learned Hidden Layer Weights (W1):\n", W1)
print("Learned Hidden Layer Biases (b1):\n", b1)
print("Learned Output Layer Weights (W2):\n", W2)
print("Learned Output Layer Bias (b2):\n", b2)
print("=" * 80)
