"""
LAB 5 - Step 3: Multilayer Perceptron for XOR in PyTorch & Decision Boundary
Topics Covered:
1. Building an MLP in PyTorch using torch.nn.Module.
2. Architecture: Linear(2, 4) -> Sigmoid() -> Linear(4, 1) -> Sigmoid().
3. PyTorch training pipeline: zero_grad(), forward(), loss.backward(), optimizer.step().
4. Binary Cross-Entropy Loss (nn.BCELoss).
5. Visualizing the Non-Linear Decision Boundary using Matplotlib contourf.
"""

import os
import warnings
warnings.filterwarnings("ignore")

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

print("=" * 80)
print("LAB 5 - PART 3: PYTORCH MULTILAYER PERCEPTRON FOR XOR")
print("=" * 80)

# XOR Dataset Tensors
X_tensor = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
], dtype=torch.float32)

y_tensor = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float32)

# 1. Define Model Architecture
class XORNet(nn.Module):
    def __init__(self):
        super(XORNet, self).__init__()
        # Single hidden layer with non-linear activation
        self.hidden = nn.Linear(in_features=2, out_features=4)
        self.act1 = nn.Sigmoid()
        self.output = nn.Linear(in_features=4, out_features=1)
        self.act2 = nn.Sigmoid()

    def forward(self, x):
        x = self.act1(self.hidden(x))
        x = self.act2(self.output(x))
        return x

# Instantiate Model, Loss Function, and Optimizer
torch.manual_seed(42)
model = XORNet()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.08)

print("PyTorch Model Architecture:")
print(model)

# 2. Training Loop
epochs = 1500
print(f"\nTraining for {epochs} epochs with Adam optimizer...")

for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    
    # Forward pass
    outputs = model(X_tensor)
    loss = criterion(outputs, y_tensor)
    
    # Backward pass & optimization
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 300 == 0:
        preds = (outputs >= 0.5).float()
        acc = (preds == y_tensor).float().mean() * 100
        print(f"Epoch [{epoch + 1:4d}/{epochs}] | BCE Loss: {loss.item():.5f} | Accuracy: {acc.item():.1f}%")

# 3. Model Evaluation
model.eval()
with torch.no_grad():
    final_preds = model(X_tensor)

print("\n--- Final PyTorch Model Evaluation on XOR ---")
print("Input (x1, x2) | Target | Model Prediction | Output Class")
print("-" * 55)
X_list = X_tensor.tolist()
y_list = y_tensor.tolist()
preds_list = final_preds.squeeze().tolist()

for (x1, x2), target, pred in zip(X_list, y_list, preds_list):
    cls = int(pred >= 0.5)
    print(f"    ({int(x1)}, {int(x2)})      |   {int(target[0])}    |     {pred:.5f}      |      {cls}")

# -----------------------------------------------------------------------------
# 4. VISUALIZE NON-LINEAR DECISION BOUNDARY
# -----------------------------------------------------------------------------
# Create a dense 2D meshgrid using NumPy
x_min, x_max = -0.5, 1.5
y_min, y_max = -0.5, 1.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 250), np.linspace(y_min, y_max, 250))
grid_coords = np.c_[xx.ravel(), yy.ravel()].tolist()
grid_tensor = torch.tensor(grid_coords, dtype=torch.float32)

with torch.no_grad():
    grid_preds_flat = model(grid_tensor).squeeze().tolist()

# Reshape back using numpy array from flat list
grid_preds = np.array(grid_preds_flat).reshape(xx.shape)

plt.figure(figsize=(8, 7))

# Contour plot of decision boundary
contour = plt.contourf(xx, yy, grid_preds, levels=50, cmap='coolwarm', alpha=0.7)
plt.colorbar(contour, label='Predicted Probability P(Y=1)')
plt.contour(xx, yy, grid_preds, levels=[0.5], colors='black', linewidths=2.5, linestyles='--')

# Plot the 4 XOR training points
for (x1, x2), target in zip(X_list, y_list):
    marker = 'o' if target[0] == 0 else 's'
    color = 'blue' if target[0] == 0 else 'red'
    plt.scatter(x1, x2, color=color, s=150, edgecolors='black', linewidth=2, zorder=10)
    plt.text(x1 + 0.05, x2 + 0.05, f"({int(x1)},{int(x2)}) -> {int(target[0])}", fontsize=11, fontweight='bold')

plt.title("MLP Non-Linear Decision Boundary for Binary XOR Function", fontsize=12, fontweight='bold')
plt.xlabel("Input Feature x1", fontsize=11)
plt.ylabel("Input Feature x2", fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)

output_img = os.path.join(os.path.dirname(__file__), "mlp_xor_decision_boundary.png")
plt.savefig(output_img, dpi=200)
plt.close()

print(f"\nNon-linear decision boundary plot saved to: {output_img}")
print("=" * 80)
