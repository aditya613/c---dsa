# Lab 6 - Part 1: PyTorch Fundamentals (Tensors & Autograd)
import torch

# 1. Tensor creation
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
print("Tensor A:", a)
print("Tensor B:", b)
print("Sum (A + B):", a + b)
print("Dot Product:", torch.dot(a, b).item())

# 2. Autograd (Automatic Differentiation)
# Let y = 3*x^2 + 2*x + 1. At x = 4, dy/dx = 6*x + 2 = 26
x = torch.tensor(4.0, requires_grad=True)
y = 3 * (x ** 2) + 2 * x + 1

# Backward pass
y.backward()
print(f"\nFunction: y = 3*x^2 + 2*x + 1")
print(f"Computed Gradient dy/dx at x=4: {x.grad.item()} (Analytical: 6*4 + 2 = 26)")
