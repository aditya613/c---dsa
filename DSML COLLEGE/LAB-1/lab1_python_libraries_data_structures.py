"""
====================================================================================================
LAB 1: PYTHON SCIENTIFIC LIBRARIES & FUNDAMENTAL DATA STRUCTURES
====================================================================================================
Objectives:
Part 1: Explore scientific computing libraries: NumPy, Pandas, Matplotlib, Scikit-learn.
Part 2: Implement and analyze fundamental data structures:
        - Dynamic Lists (slicing, mutations, comprehensions)
        - Dictionaries (hash lookups, nested mappings, dict comprehensions)
        - Sets (uniqueness, hash properties, mathematical set algebra)
        - Stacks (LIFO simulation, overflow/underflow, bracket balancing)
        - Queues (FIFO simulation, O(n) list vs O(1) deque performance benchmark)
====================================================================================================
"""

import os
import time
from collections import deque
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ==================================================================================================
# PART 1: EXPLORATION OF CORE SCIENTIFIC LIBRARIES
# ==================================================================================================
print("=" * 85)
print("PART 1: SCIENTIFIC COMPUTING LIBRARIES (NUMPY, PANDAS, MATPLOTLIB, SCIKIT-LEARN)")
print("=" * 85)

# --- 1.1 NumPy: Vectorized Computing & Broadcasting ---
print("\n[1.1 NumPy Vectorization & Broadcasting]")
np.random.seed(42)
matrix_a = np.arange(1, 10, dtype=float).reshape(3, 3)
vector_b = np.array([10.0, 20.0, 30.0])

# Broadcasting: vector_b is virtually stretched across rows of matrix_a without memory duplication
broadcasted_sum = matrix_a + vector_b
dot_product = np.dot(matrix_a, vector_b)

print("Matrix A (3x3):\n", matrix_a)
print("Vector B (1x3):\n", vector_b)
print("Broadcasting Sum (Matrix A + Vector B):\n", broadcasted_sum)
print(f"Matrix-Vector Dot Product: {dot_product}")
print(f"Matrix Statistics -> Mean: {matrix_a.mean():.2f}, Std Dev: {matrix_a.std():.2f}")

# --- 1.2 Pandas: Tabular Data Manipulation ---
print("\n[1.2 Pandas Tabular Data]")
data = {
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Aditya", "Bhavna", "Chirag", "Deepak", "Esha"],
    "Department": ["CS", "AI", "CS", "Data Science", "AI"],
    "GPA": [9.4, 8.8, 7.9, 9.1, 8.5],
    "Attendance": [95, 88, 74, 92, 85]
}
df_students = pd.DataFrame(data)
print("Student Records DataFrame:")
print(df_students)

# SQL-like GroupBy Aggregation
dept_summary = df_students.groupby("Department")["GPA"].agg(["count", "mean", "max"]).reset_index()
print("\nDepartment-wise GPA Summary:")
print(dept_summary)

# --- 1.3 Scikit-Learn: Machine Learning Pipeline ---
print("\n[1.3 Scikit-Learn Classical ML]")
# Generate synthetic 2-feature classification dataset
X_synthetic = np.random.randn(200, 2)
# Decision boundary: x0 + x1 > 0
y_synthetic = (X_synthetic[:, 0] + X_synthetic[:, 1] > 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X_synthetic, y_synthetic, test_size=0.25, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)
preds = clf.predict(X_test_scaled)
acc = accuracy_score(y_test, preds)
print(f"Trained LogisticRegression -> Test Set Accuracy: {acc*100:.2f}%")

# --- 1.4 Matplotlib: Visualization Panel ---
script_dir = os.path.dirname(os.path.abspath(__file__))
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Feature Scatter with Decision Classes
axes[0].scatter(X_synthetic[y_synthetic == 0, 0], X_synthetic[y_synthetic == 0, 1],
                color='crimson', label='Class 0', alpha=0.7, edgecolors='k')
axes[0].scatter(X_synthetic[y_synthetic == 1, 0], X_synthetic[y_synthetic == 1, 1],
                color='teal', label='Class 1', alpha=0.7, edgecolors='k')
axes[0].set_title("Scikit-Learn Synthetic Classification Space", fontweight='bold')
axes[0].set_xlabel("Feature 1")
axes[0].set_ylabel("Feature 2")
axes[0].legend()
axes[0].grid(True, linestyle=":", alpha=0.6)

# Plot 2: Department GPA Bar Chart
axes[1].bar(dept_summary["Department"], dept_summary["mean"], color=['#4C72B0', '#55A868', '#C44E52'], edgecolor='k')
axes[1].set_title("Pandas Aggregated Mean GPA by Department", fontweight='bold')
axes[1].set_ylabel("Mean GPA")
axes[1].set_ylim(0, 10)
axes[1].grid(axis='y', linestyle=":", alpha=0.6)

plt.tight_layout()
out_plot = os.path.join(script_dir, "lib_exploration_plot.png")
plt.savefig(out_plot, dpi=300)
plt.close()
print(f"Saved visualization panel to: {out_plot}")

# ==================================================================================================
# PART 2: FUNDAMENTAL PYTHON DATA STRUCTURES
# ==================================================================================================
print("\n" + "=" * 85)
print("PART 2: CORE PYTHON DATA STRUCTURES & TIME COMPLEXITY")
print("=" * 85)

# --- 2.1 Dynamic List Operations ---
print("\n--- 2.1 LIST MANIPULATION ---")
nums = [15, 3, 22, 8, 45, 12, 9]
print(f"Initial List: {nums}")

# Slicing, insertion, removal
nums.append(50)                  # O(1) amortized
nums.insert(2, 99)               # O(n) element shift
removed_val = nums.pop()         # O(1) from end
nums.sort()                      # O(n log n) Timsort
print(f"After Insert(idx 2, 99), Append(50), Pop(), and Sort(): {nums}")

# List Comprehension for feature min-max normalization
min_n, max_n = min(nums), max(nums)
normalized_nums = [(x - min_n) / (max_n - min_n) for x in nums]
print(f"List Comprehension Normalized [0, 1]: {[round(x, 3) for x in normalized_nums]}")

# --- 2.2 Hash Map / Dictionary Operations ---
print("\n--- 2.2 DICTIONARY (HASH MAP) OPERATIONS ---")
phonebook = {
    "Aditya": {"phone": "9876543210", "role": "ML Engineer"},
    "Bhavna": {"phone": "9123456780", "role": "Data Analyst"}
}
# Safe retrieval with fallback
print("Aditya's Role:", phonebook["Aditya"]["role"])
print("Lookup non-existing key (Safe .get()):", phonebook.get("Rohan", "Contact Not Found"))

# Dictionary Comprehension (Class label to integer index encoder)
classes = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
label_to_id = {cls_name: idx for idx, cls_name in enumerate(classes)}
print("Label-to-Index Mapping (Dict Comprehension):", label_to_id)

# --- 2.3 Set Properties & Mathematical Set Algebra ---
print("\n--- 2.3 SET PROPERTIES & ALGEBRA ---")
raw_tags = ["python", "ml", "python", "ai", "deep learning", "ml", "pandas"]
unique_tags = set(raw_tags)
print(f"Raw tags with duplicates ({len(raw_tags)}): {raw_tags}")
print(f"Deduplicated Set ({len(unique_tags)}): {unique_tags}")

ai_skills = {"python", "pytorch", "math", "statistics", "machine learning"}
web_skills = {"python", "javascript", "react", "html", "css"}

print(f"Union (All Skills)                    : {ai_skills | web_skills}")
print(f"Intersection (Common Skills)          : {ai_skills & web_skills}")
print(f"Difference (AI only, not Web)         : {ai_skills - web_skills}")
print(f"Symmetric Difference (Non-overlapping): {ai_skills ^ web_skills}")

# --- 2.4 Stack Implementation (LIFO) ---
print("\n--- 2.4 STACK (LIFO) SIMULATION ---")

class Stack:
    """Encapsulated Stack adhering strictly to LIFO semantics."""
    def __init__(self, capacity=10):
        self._items = []
        self._capacity = capacity

    def push(self, item):
        if len(self._items) >= self._capacity:
            raise OverflowError("Stack Overflow: Maximum capacity reached.")
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from empty stack.")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

stack = Stack(capacity=5)
for elem in ["Page 1", "Page 2", "Page 3"]:
    stack.push(elem)
    print(f"Pushed: {elem} | Current Top: {stack.peek()}")

print(f"Popped: {stack.pop()} (LIFO order)")
print(f"Current Stack Size: {stack.size()}, Top Element: {stack.peek()}")

# Application: Balanced Parentheses Checker using Stack
def is_balanced(expression):
    s = Stack(capacity=len(expression) + 1)
    mapping = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in mapping.values():
            s.push(char)
        elif char in mapping.keys():
            if s.is_empty() or s.pop() != mapping[char]:
                return False
    return s.is_empty()

expr1 = "{[a + b] * (c - d)}"
expr2 = "{[a + b] * (c - d)"
print(f"Parentheses Check '{expr1}': {'Balanced' if is_balanced(expr1) else 'Unbalanced'}")
print(f"Parentheses Check '{expr2}': {'Balanced' if is_balanced(expr2) else 'Unbalanced'}")

# --- 2.5 Queue Implementation (FIFO) & Benchmarking ---
print("\n--- 2.5 QUEUE (FIFO) & BENCHMARKING (LIST vs DEQUE) ---")

class Queue:
    """Encapsulated FIFO Queue using collections.deque for O(1) amortized operations."""
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("Queue Underflow: Cannot dequeue from empty queue.")
        return self._items.popleft()

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

q = Queue()
for job in ["Job_A", "Job_B", "Job_C"]:
    q.enqueue(job)
    print(f"Enqueued: {job}")

print(f"Dequeued: {q.dequeue()} (FIFO order)")
print(f"Dequeued: {q.dequeue()} (FIFO order)")
print(f"Remaining in Queue: {q.size()}")

# Benchmarking: Why list.pop(0) is O(n) while deque.popleft() is O(1)
N = 50000
list_q = list(range(N))
deque_q = deque(range(N))

# Benchmark List pop(0)
t0 = time.perf_counter()
for _ in range(10000):
    list_q.pop(0)  # Requires shifting remaining elements in contiguous memory
t_list = time.perf_counter() - t0

# Benchmark Deque popleft()
t0 = time.perf_counter()
for _ in range(10000):
    deque_q.popleft()  # Directly updates doubly-linked chunk pointer
t_deque = time.perf_counter() - t0

print(f"\nBenchmark (10,000 Dequeue operations on {N}-element structure):")
print(f"  -> Python list.pop(0)       : {t_list:.4f} seconds (O(n) linear memory shifts)")
print(f"  -> collections.deque.popleft(): {t_deque:.4f} seconds (O(1) pointer adjustment)")
print(f"  -> Deque Speedup Factor     : {t_list / t_deque:.1f}x FASTER!")

print("\n" + "=" * 85)
print("LAB 1 COMPLETED SUCCESSFULLY!")
print("=" * 85)
