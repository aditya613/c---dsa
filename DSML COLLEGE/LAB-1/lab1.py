# ============================================================
# LAB 1: Python Scientific Libraries & Basic Data Structures
# ============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NumPy: Array creation and vector calculations
arr = np.array([10, 20, 30, 40, 50])
print("1. NumPy Array:", arr)
print(f"   Mean: {arr.mean():.1f}, Sum: {arr.sum()}")

# 2. Pandas: Series and DataFrame
df = pd.DataFrame({
    "Student": ["Aditya", "Rohan", "Pooja"],
    "Score": [88, 92, 79]
})
print("\n2. Pandas DataFrame:\n", df)

# 3. Matplotlib: Simple plot
plt.figure(figsize=(5, 3))
plt.plot([1, 2, 3, 4], [10, 25, 20, 35], marker='o', color='blue')
plt.title("Lab 1: Matplotlib Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.savefig("lab1_plot.png")
print("\n3. Matplotlib: Plot saved to 'lab1_plot.png'")

# 4. List Operations
lst = ["apple", "banana", "cherry"]
lst.append("orange")      # Add at end
lst.insert(1, "mango")    # Insert at index 1
lst.remove("banana")      # Remove by value
popped = lst.pop()        # Remove from end
print(f"\n4. List Operations: Popped '{popped}', Final List:", lst)

# 5. Dictionary Operations (Key-Value)
student = {"name": "Aditya", "roll": 101, "course": "DSML"}
student["marks"] = 95     # Add new key
print(f"\n5. Dictionary: {student}")
print(f"   Lookup 'name': {student['name']}")

# 6. Set Operations (Unique & Unordered)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"\n6. Sets: A = {set_a}, B = {set_b}")
print(f"   Union (A | B):        {set_a | set_b}")
print(f"   Intersection (A & B): {set_a & set_b}")

# 7. Stack Simulation (LIFO - Last In, First Out)
stack = []
stack.append("Book 1")    # Push
stack.append("Book 2")    # Push
print(f"\n7. Stack after pushes: {stack}")
print(f"   Popped from Stack:  {stack.pop()}")  # Pop Book 2
print(f"   Stack now:          {stack}")

# 8. Queue Simulation (FIFO - First In, First Out)
queue = []
queue.append("Person 1")  # Enqueue
queue.append("Person 2")  # Enqueue
print(f"\n8. Queue after enqueues: {queue}")
print(f"   Dequeued from Queue:  {queue.pop(0)}")  # Dequeue Person 1
print(f"   Queue now:            {queue}")
