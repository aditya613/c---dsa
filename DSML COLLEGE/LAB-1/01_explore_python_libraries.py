# Lab 1 - Part 1: Basic Python Libraries for Data Science
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. NumPy: Arrays and basic operations
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))

# 2. Pandas: Series and DataFrame
data = {
    "Name": ["Aditya", "Rohan", "Pooja"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# 3. Matplotlib: Simple Line Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, marker='o')
plt.title("Simple Matplotlib Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.savefig("simple_plot.png")
print("\nPlot saved as 'simple_plot.png'")

# 4. Scikit-Learn: Simple Linear Fit
X_train = np.array([[1], [2], [3], [4]])
y_train = np.array([2, 4, 6, 8])
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict([[5]])
print("Scikit-Learn Prediction for 5:", pred[0])
