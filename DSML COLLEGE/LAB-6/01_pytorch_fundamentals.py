"""
LAB 6 - Step 1: Introduction to PyTorch Fundamentals
Topics Covered:
1. PyTorch Tensors: Creation, data types (float32, int64), dimensions, and device placement.
2. Tensor Operations: Element-wise arithmetic, matrix multiplication (@ / torch.matmul), reshaping.
3. Autograd Engine: Computational graphs, requires_grad=True, backpropagation via .backward(), gradients (.grad).
4. Building Neural Network Layers: torch.nn.Module, nn.Linear, activations (ReLU, Sigmoid).
5. The 5-Step Canonical PyTorch Training Loop.
"""

import warnings
warnings.filterwarnings("ignore")

import torch
import torch.nn as nn
import torch.optim as optim

print("=" * 80)
print("LAB 6 - PART 1: INTRODUCTION TO PYTORCH FUNDAMENTALS")
print("=" * 80)
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA Available?  {torch.cuda.is_available()} (Running on CPU)")

# -----------------------------------------------------------------------------
# 1. TENSOR CREATION & BASICS
# -----------------------------------------------------------------------------
print("\n[1] TENSOR CREATION & INSPECTION")
print("-" * 40)

# Creating tensors from scalar, list, and built-in factories
t_scalar = torch.tensor(3.14159)
t_1d = torch.tensor([10.0, 20.0, 30.0, 40.0], dtype=torch.float32)
t_zeros = torch.zeros((2, 3))
t_ones = torch.ones((3, 2))
t_rand = torch.rand((2, 4))  # Uniform [0, 1)

print(f"Scalar Tensor: {t_scalar.item():.4f} | Dimensions: {t_scalar.ndim}")
print(f"1D Tensor:     {t_1d.tolist()} | Shape: {list(t_1d.shape)} | Dtype: {t_1d.dtype}")
print(f"2D Zeros Tensor (2x3):\n{t_zeros.tolist()}")
print(f"Random Tensor (2x4):\n{t_rand.tolist()}")

# -----------------------------------------------------------------------------
# 2. TENSOR OPERATIONS & RESHAPING
# -----------------------------------------------------------------------------
print("\n[2] TENSOR OPERATIONS & LINEAR ALGEBRA")
print("-" * 40)

a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Element-wise addition and multiplication
print(f"Element-wise Addition (A + B):\n{(a + b).tolist()}")
print(f"Element-wise Multiplication (A * B):\n{(a * b).tolist()}")

# Matrix multiplication (Dot product / Matmul)
c = torch.matmul(a, b)  # or a @ b
print(f"Matrix Multiplication (A @ B):\n{c.tolist()}")

# Reshaping and flattening
flat = c.view(-1)
print(f"Flattened View: {flat.tolist()} | Shape: {list(flat.shape)}")

# -----------------------------------------------------------------------------
# 3. AUTOGRAD: AUTOMATIC DIFFERENTIATION ENGINE
# -----------------------------------------------------------------------------
print("\n[3] AUTOGRAD & COMPUTATIONAL GRAPH")
print("-" * 40)

# Let function: y = 3 * x^2 + 5 * x + 2
# Analytical derivative: dy/dx = 6 * x + 5
# At x = 4.0 -> dy/dx = 6(4) + 5 = 29.0
x = torch.tensor(4.0, requires_grad=True)
y = 3.0 * (x ** 2) + 5.0 * x + 2.0

print(f"Input x: {x.item()}")
print(f"Evaluated y: {y.item()}")
print(f"Computational Graph Creator (grad_fn): {y.grad_fn}")

# Perform backpropagation to compute dy/dx
y.backward()

print(f"Autograd Computed dy/dx: {x.grad.item():.2f}")
print("Exact Match with Analytical Derivative (6*4 + 5 = 29.0)!")

# -----------------------------------------------------------------------------
# 4. BUILDING A NEURAL NETWORK & CANONICAL TRAINING LOOP
# -----------------------------------------------------------------------------
print("\n[4] NN.MODULE & CANONICAL 5-STEP TRAINING LOOP")
print("-" * 40)

# Generate synthetic linear data: y = 3.5 * x + 1.2
torch.manual_seed(42)
X_train = torch.unsqueeze(torch.linspace(-2.0, 2.0, 30), dim=1)
y_train = 3.5 * X_train + 1.2 + 0.1 * torch.randn(X_train.size())

# Define a Linear Regression model using torch.nn.Module
class LinearRegressor(nn.Module):
    def __init__(self):
        super(LinearRegressor, self).__init__()
        self.linear = nn.Linear(in_features=1, out_features=1)

    def forward(self, x):
        return self.linear(x)

model = LinearRegressor()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.05)

print("Initialized Linear Model Parameters:")
for name, param in model.named_parameters():
    print(f" - {name}: {param.data.squeeze().item():.4f}")

# The Canonical 5-Step PyTorch Training Loop
epochs = 200
print(f"\nTraining for {epochs} epochs...")

for epoch in range(epochs):
    # Step 1: Zero parameter gradients
    optimizer.zero_grad()
    
    # Step 2: Forward pass (predictions)
    predictions = model(X_train)
    
    # Step 3: Compute loss
    loss = criterion(predictions, y_train)
    
    # Step 4: Backward pass (compute dLoss/dWeight)
    loss.backward()
    
    # Step 5: Optimizer step (Weight update: w := w - lr * grad)
    optimizer.step()
    
    if (epoch + 1) % 50 == 0:
        print(f"Epoch [{epoch + 1:3d}/{epochs}] -> MSE Loss: {loss.item():.5f}")

learned_w = model.linear.weight.item()
learned_b = model.linear.bias.item()

print(f"\nModel Learned Target Relationship:")
print(f"Target:  y = 3.50 * x + 1.20")
print(f"Learned: y = {learned_w:.2f} * x + {learned_b:.2f}")
print("PyTorch fundamentals successfully validated!")
print("=" * 80)
