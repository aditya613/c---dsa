# LAB 5: Multilayer Perceptron (MLP) for XOR Classification
import numpy as np
from sklearn.neural_network import MLPClassifier

# 1. XOR Dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# 2. Multilayer Perceptron with hidden layer
# solver='lbfgs' is ideal for small datasets to guarantee convergence
mlp = MLPClassifier(hidden_layer_sizes=(4,), activation='logistic', solver='lbfgs', random_state=42)
mlp.fit(X, y)

# 3. Predict on XOR inputs
predictions = mlp.predict(X)
probabilities = mlp.predict_proba(X)[:, 1]

print("--- MLP XOR Classification Results ---")
for i in range(len(X)):
    print(f"Input: {X[i]} | True y: {y[i]} | Predicted: {predictions[i]} | Probability: {probabilities[i]:.4f}")

accuracy = np.mean(predictions == y) * 100
print(f"\nFinal Classification Accuracy: {accuracy:.1f}%")
print("MLP successfully solves the XOR problem by creating a non-linear decision boundary!")
