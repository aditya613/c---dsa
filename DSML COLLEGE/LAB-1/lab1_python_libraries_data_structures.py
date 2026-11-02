# LAB 1: Python Libraries & Basic Data Structures
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("--- 1. NumPy Array Operations ---")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print(f"Mean: {arr.mean()}, Sum: {arr.sum()}")

print("\n--- 2. Pandas DataFrame ---")
df = pd.DataFrame({"Name": ["Aditya", "Rohan", "Pooja"], "Marks": [85, 92, 78]})
print(df)

print("\n--- 3. Matplotlib Line Plot ---")
plt.plot([1, 2, 3, 4], [10, 20, 15, 30], marker='o')
plt.title("Sample Line Plot")
plt.savefig("lib_exploration_plot.png")
print("Saved plot to 'lib_exploration_plot.png'")

print("\n--- 4. List Operations ---")
lst = [10, 20, 30]
lst.append(40)
lst.insert(1, 15)
print("List after append & insert:", lst)
print("Popped item:", lst.pop())

print("\n--- 5. Dictionary Operations ---")
d = {"name": "Aditya", "course": "DSML"}
d["semester"] = 5
print("Dictionary:", d)
print("Access key 'name':", d["name"])

print("\n--- 6. Set Operations ---")
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("Set A:", s1, "| Set B:", s2)
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)

print("\n--- 7. Stack Simulation (LIFO) ---")
stack = []
stack.append("A")
stack.append("B")
print("Stack:", stack)
print("Popped:", stack.pop())

print("\n--- 8. Queue Simulation (FIFO) ---")
queue = []
queue.append("First")
queue.append("Second")
print("Queue:", queue)
print("Dequeued:", queue.pop(0))
