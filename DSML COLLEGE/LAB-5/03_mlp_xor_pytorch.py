# Lab 5 - Part 3: MLP for XOR using PyTorch
import torch
import torch.nn as nn
import torch.optim as optim

# XOR Data
X = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = torch.tensor([[0.0], [1.0], [1.0], [0.0]])

# Define simple MLP: 2 inputs -> 2 hidden -> 1 output
model = nn.Sequential(
    nn.Linear(2, 2),
    nn.Sigmoid(),
    nn.Linear(2, 1),
    nn.Sigmoid()
)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.1)

# Training loop
for epoch in range(1000):
    optimizer.zero_grad()
    predictions = model(X)
    loss = criterion(predictions, y)
    loss.backward()
    optimizer.step()

print("--- PyTorch MLP XOR Output ---")
with torch.no_grad():
    preds = model(X)
    for i in range(len(X)):
        print(f"Input: {X[i].numpy()} -> Prob: {preds[i].item():.4f} -> Class: {int(preds[i].item() >= 0.5)}")
