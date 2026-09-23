"""
====================================================================================================
LAB 5: MULTILAYER PERCEPTRON (MLP) FOR BINARY XOR CLASSIFICATION
====================================================================================================
Objectives:
1. Prove mathematically and demonstrate experimentally why a Single-Layer Perceptron fails on XOR.
2. Implement a Multilayer Perceptron (MLP) with non-linear Sigmoid activation from scratch
   in pure NumPy using full analytical backpropagation (chain rule).
3. Implement the MLP architecture in PyTorch using nn.Module, BCELoss, and optim.Adam.
4. Visualize the learned non-linear decision boundary separating the XOR truth table.
====================================================================================================
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim

# Set reproducible seeds
np.random.seed(1)
torch.manual_seed(42)

# XOR Truth Table Dataset
X_xor = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]], dtype=float)

y_xor = np.array([[0],
                  [1],
                  [1],
                  [0]], dtype=float)

# --------------------------------------------------------------------------------------------------
# STEP 1: EXPERIMENTAL PROOF - SINGLE-LAYER PERCEPTRON FAILURE
# --------------------------------------------------------------------------------------------------
print("=" * 85)
print("STEP 1: DEMONSTRATING THE FAILURE OF A SINGLE-LAYER PERCEPTRON ON XOR")
print("=" * 85)
print("Mathematical Context: XOR is non-linearly separable. Minsky & Papert (1969) proved")
print("that no linear hyperplane w1*x1 + w2*x2 + b = 0 can separate (0,1),(1,0) from (0,0),(1,1).")

w_single = np.random.randn(2, 1)
b_single = np.random.randn(1)
lr_single = 0.1

for epoch in range(100):
    linear_out = np.dot(X_xor, w_single) + b_single
    preds = (linear_out >= 0).astype(int)
    errors = y_xor - preds
    w_single += lr_single * np.dot(X_xor.T, errors)
    b_single += lr_single * np.sum(errors)

final_preds = ((np.dot(X_xor, w_single) + b_single) >= 0).astype(int)
acc_single = np.mean(final_preds == y_xor) * 100
print(f"Final Single-Layer Perceptron Predictions on XOR:\n{final_preds.flatten()} vs Expected {y_xor.flatten()}")
print(f"Single-Layer Perceptron Accuracy: {acc_single:.1f}% (FAILED to solve XOR!)")

# --------------------------------------------------------------------------------------------------
# STEP 2: MULTILAYER PERCEPTRON (MLP) FROM SCRATCH IN NUMPY
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 2: MULTILAYER PERCEPTRON (NUMPY WITH ANALYTICAL BACKPROPAGATION)")
print("=" * 85)

# Sigmoid activation and derivative
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -250, 250)))

def sigmoid_derivative(a):
    return a * (1.0 - a)

# Initialize network architecture: 2 inputs -> 4 hidden neurons -> 1 output neuron
hidden_dim = 4
W1 = np.random.uniform(-1, 1, (2, hidden_dim))
b1 = np.zeros((1, hidden_dim))
W2 = np.random.uniform(-1, 1, (hidden_dim, 1))
b2 = np.zeros((1, 1))

learning_rate = 0.5
epochs = 10000
loss_history_numpy = []

for epoch in range(epochs):
    # Forward Pass
    Z1 = np.dot(X_xor, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)  # y_hat
    
    # Binary Cross-Entropy Loss
    loss = -np.mean(y_xor * np.log(A2 + 1e-15) + (1 - y_xor) * np.log(1 - A2 + 1e-15))
    loss_history_numpy.append(loss)
    
    # Backward Pass (Analytical Chain Rule)
    # Output layer delta: dL/dZ2 = A2 - y
    delta2 = A2 - y_xor
    dW2 = np.dot(A1.T, delta2) / len(X_xor)
    db2 = np.sum(delta2, axis=0, keepdims=True) / len(X_xor)
    
    # Hidden layer delta: dL/dZ1 = (delta2 * W2^T) element-wise-mult sigmoid'(Z1)
    delta1 = np.dot(delta2, W2.T) * sigmoid_derivative(A1)
    dW1 = np.dot(X_xor.T, delta1) / len(X_xor)
    db1 = np.sum(delta1, axis=0, keepdims=True) / len(X_xor)
    
    # Gradient updates
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

print("NumPy MLP Training Completed!")
print("Final Probabilities [y_hat]:\n", np.round(A2, 4).flatten())
binary_preds_np = (A2 >= 0.5).astype(int).flatten()
print("Binary Predictions (threshold 0.5):\n", binary_preds_np)
acc_numpy = np.mean((A2 >= 0.5).astype(int) == y_xor) * 100
print(f"NumPy Scratch MLP Accuracy: {acc_numpy:.1f}% (SUCCESSFULLY SOLVED XOR!)")

# --------------------------------------------------------------------------------------------------
# STEP 3: PYTORCH IMPLEMENTATION & TRAINING
# --------------------------------------------------------------------------------------------------
print("\n" + "=" * 85)
print("STEP 3: PYTORCH IMPLEMENTATION (NN.MODULE, BCELOSS & ADAM)")
print("=" * 85)

X_tensor = torch.tensor(X_xor, dtype=torch.float32)
y_tensor = torch.tensor(y_xor, dtype=torch.float32)

class XOR_MLP(nn.Module):
    def __init__(self):
        super(XOR_MLP, self).__init__()
        self.hidden = nn.Linear(2, 4)     # 2 inputs to 4 hidden units
        self.act1 = nn.Sigmoid()
        self.output = nn.Linear(4, 1)     # 4 hidden units to 1 output
        self.act2 = nn.Sigmoid()

    def forward(self, x):
        h = self.act1(self.hidden(x))
        out = self.act2(self.output(h))
        return out

model_pt = XOR_MLP()
criterion = nn.BCELoss()
optimizer = optim.Adam(model_pt.parameters(), lr=0.08)

loss_history_pt = []
for epoch in range(1500):
    optimizer.zero_grad()
    preds_pt = model_pt(X_tensor)
    loss = criterion(preds_pt, y_tensor)
    loss.backward()
    optimizer.step()
    loss_history_pt.append(loss.item())

with torch.no_grad():
    test_preds = model_pt(X_tensor)
    # Use tolist() to avoid NumPy 2.x tensor conversion compatibility
    pred_vals = np.array(test_preds.tolist()).flatten()
    binary_preds = (pred_vals >= 0.5).astype(int)
    print("PyTorch Final Predicted Probabilities:\n", np.round(pred_vals, 4))
    print("PyTorch Binary Predictions:\n", binary_preds)
    print(f"PyTorch Accuracy: {np.mean(binary_preds == y_xor.flatten())*100:.1f}% (SUCCESSFULLY SOLVED XOR!)")

# --------------------------------------------------------------------------------------------------
# STEP 4: VISUALIZATION OF NON-LINEAR DECISION BOUNDARY
# --------------------------------------------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
fig.suptitle("Multilayer Perceptron: Solving the Non-Linear XOR Problem", fontsize=15, fontweight='bold')

# Panel 1: Decision Boundary
ax1 = axes[0]
xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 300), np.linspace(-0.5, 1.5, 300))
grid_points = torch.tensor(np.c_[xx.ravel(), yy.ravel()], dtype=torch.float32)

with torch.no_grad():
    grid_out = model_pt(grid_points)
    Z_grid = np.array(grid_out.tolist()).reshape(xx.shape)

contour = ax1.contourf(xx, yy, Z_grid, levels=50, cmap='Spectral', alpha=0.8)
ax1.contour(xx, yy, Z_grid, levels=[0.5], colors='black', linewidths=2.5, linestyles='--')
cbar = fig.colorbar(contour, ax=ax1)
cbar.set_label("Predicted Output Probability P(y=1)", rotation=270, labelpad=15)

# Plot actual XOR points
colors = ['red' if y == 0 else 'blue' for y in y_xor.flatten()]
for i in range(len(X_xor)):
    ax1.scatter(X_xor[i, 0], X_xor[i, 1], c=colors[i], edgecolors='white', s=160,
                marker='o' if y_xor[i] == 0 else '^', zorder=5)

ax1.scatter([], [], c='red', marker='o', edgecolors='white', s=100, label='Class 0 (0,0 & 1,1)')
ax1.scatter([], [], c='blue', marker='^', edgecolors='white', s=100, label='Class 1 (0,1 & 1,0)')
ax1.plot([], [], 'k--', lw=2, label='Decision Boundary (P = 0.5)')
ax1.set_title("Learned Non-Linear Decision Boundary", fontweight='bold')
ax1.set_xlabel("Input Feature x1")
ax1.set_ylabel("Input Feature x2")
ax1.legend(loc="upper right")

# Panel 2: Training Loss Convergence
ax2 = axes[1]
ax2.plot(loss_history_pt, color='purple', lw=2, label='PyTorch BCELoss')
ax2.set_title("Training Loss Convergence Curve", fontweight='bold')
ax2.set_xlabel("Epochs")
ax2.set_ylabel("Binary Cross-Entropy Loss")
ax2.legend()
ax2.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
out_plot = os.path.join(script_dir, "mlp_xor_decision_boundary.png")
plt.savefig(out_plot, dpi=300)
plt.close()

print(f"\nDecision boundary figure saved to:\n -> {out_plot}")
print("=" * 85)
print("LAB 5 COMPLETED SUCCESSFULLY!")
print("=" * 85)
