# Lab 3 - Part 1: Feature Scaling Techniques (Min-Max, Standard, Robust)
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# Sample data with one extreme outlier (1000)
data = np.array([[10], [20], [30], [40], [1000]])

# 1. Min-Max Scaler (Binds values strictly to [0, 1])
minmax = MinMaxScaler()
data_minmax = minmax.fit_transform(data)

# 2. Standard Scaler (Transforms to Mean=0, Std=1)
std_scaler = StandardScaler()
data_std = std_scaler.fit_transform(data)

# 3. Robust Scaler (Uses Median & IQR, immune to outlier)
robust = RobustScaler()
data_robust = robust.fit_transform(data)

print("Original Data:\n", data.flatten())
print("\nMin-Max Scaled [0, 1]:\n", np.round(data_minmax.flatten(), 2))
print("\nStandard Scaled (Z-Score):\n", np.round(data_std.flatten(), 2))
print("\nRobust Scaled (Median & IQR):\n", np.round(data_robust.flatten(), 2))
