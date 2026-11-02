# Lab 5 - Part 2: Multilayer Perceptron (MLP) for XOR from Scratch in NumPy
import numpy as np

# Sigmoid Activation and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# XOR Dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize random weights and biases
np.random.seed(42)
w1 = np.random.uniform(size=(2, 2))  # weights from input to hidden
b1 = np.random.uniform(size=(1, 2))
w2 = np.random.uniform(size=(2, 1))  # weights from hidden to output
b2 = np.random.uniform(size=(1, 1))
lr = 0.5

# Training loop
for epoch in range(10000):
    # Forward Pass
    hidden_input = np.dot(X, w1) + b1
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, w2) + b2
    output = sigmoid(final_input)
    
    # Backward Pass (Error & Gradients)
    error = y - output
    d_output = error * sigmoid_deriv(output)
    d_hidden = d_output.dot(w2.T) * sigmoid_deriv(hidden_output)
    
    # Update weights and biases
    w2 += hidden_output.T.dot(d_output) * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr
    w1 += X.T.dot(d_hidden) * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr

print("--- Trained MLP Predictions on XOR ---")
for i in range(len(X)):
    print(f"Input: {X[i]} -> Predicted Probability: {output[i][0]:.4f} -> Class: {int(output[i][0] >= 0.5)}")
