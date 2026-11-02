# Lab 5 - Part 1: Failure of Single-Layer Perceptron on XOR
import numpy as np
from sklearn.linear_model import Perceptron

# XOR Input and Target
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Single-layer Perceptron (Linear classifier)
model = Perceptron(max_iter=100)
model.fit(X, y)
predictions = model.predict(X)

print("XOR Inputs:\n", X)
print("Actual XOR Targets:   ", y)
print("Perceptron Predictions:", predictions)
print("Accuracy:             ", np.mean(predictions == y) * 100, "%")
print("Conclusion: A single-layer perceptron CANNOT solve XOR because XOR is non-linearly separable.")
