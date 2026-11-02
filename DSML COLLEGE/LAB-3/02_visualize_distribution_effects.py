# Lab 3 - Part 2: Visualize Scaling Effects
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Generate random feature
np.random.seed(42)
x = np.random.exponential(scale=10, size=100).reshape(-1, 1)

# Apply scalers
x_std = StandardScaler().fit_transform(x)
x_minmax = MinMaxScaler().fit_transform(x)

# Simple plot comparing original vs scaled
plt.figure(figsize=(9, 3))

plt.subplot(1, 3, 1)
plt.hist(x, bins=15, color='gray')
plt.title("Original Data")

plt.subplot(1, 3, 2)
plt.hist(x_minmax, bins=15, color='green')
plt.title("Min-Max Scaled [0, 1]")

plt.subplot(1, 3, 3)
plt.hist(x_std, bins=15, color='blue')
plt.title("Standard Scaled (Z-Score)")

plt.tight_layout()
plt.savefig("feature_scaling_distributions.png")
print("Saved distribution plot as 'feature_scaling_distributions.png'")
