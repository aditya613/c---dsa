# ============================================================
# LAB 5: Multilayer Perceptron (MLP) for Binary XOR Function
# Dataset Used: XOR Truth Table (Binary Classification)
# ============================================================
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier

# 1. The XOR Truth Table Dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

print("1. XOR Truth Table:")
for i in range(len(X)):
    print(f"   Input: {X[i]} -> Target: {y[i]}")

# 2. Step 1: Demonstrate Single-Layer Perceptron Failure
# A single-layer perceptron only learns a linear decision boundary
single_layer = Perceptron(max_iter=100)
single_layer.fit(X, y)
single_preds = single_layer.predict(X)
single_acc = np.mean(single_preds == y) * 100

print("\n2. Single-Layer Perceptron (Linear Model):")
print(f"   Predictions: {single_preds}")
print(f"   Accuracy:    {single_acc:.1f}% -> FAILS because XOR is NOT linearly separable!")

# 3. Step 2: Solve XOR with Multilayer Perceptron (MLP)
# By adding a hidden layer with non-linear activation ('logistic' / Sigmoid),
# the network maps inputs into a higher-dimensional space where they become separable.
mlp = MLPClassifier(hidden_layer_sizes=(4,), activation='logistic', solver='lbfgs', random_state=1)
mlp.fit(X, y)

mlp_preds = mlp.predict(X)
mlp_probs = mlp.predict_proba(X)[:, 1]
mlp_acc = np.mean(mlp_preds == y) * 100

print("\n3. Multilayer Perceptron (MLP with 1 Hidden Layer):")
for i in range(len(X)):
    print(f"   Input: {X[i]} | True: {y[i]} | Predicted: {mlp_preds[i]} | Prob: {mlp_probs[i]:.4f}")

print(f"\n[+] MLP Final Accuracy: {mlp_acc:.1f}% -> SUCCESSFULLY SOLVED XOR!")
