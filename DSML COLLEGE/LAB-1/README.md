# LAB 1: Python Libraries & Fundamental Data Structures for DSML

## 1. Overview & Objectives
This laboratory establishes the core computational foundations for Data Science and Machine Learning (DSML). The objectives are divided into two parts:
1. **Part 1**: Explore modern Python scientific computing libraries: **NumPy**, **Pandas**, **Matplotlib**, and **Scikit-learn**.
2. **Part 2**: Implement and analyze core Python linear and non-linear data structures:
   - Dynamic List manipulation
   - Dictionary key-value mappings
   - Set properties and mathematical set operations
   - Stack (LIFO) simulation
   - Queue (FIFO) simulation and amortized complexity analysis

---

## 2. Theoretical Foundations

### 2.1 Core Scientific Libraries
- **NumPy (Numerical Python)**: Provides contiguous $N$-dimensional array objects (`ndarray`), fast vectorization, broadcasting semantics, and optimized C/Fortran linear algebra kernels (BLAS/LAPACK).
- **Pandas**: Offers high-level spreadsheet-like structures (`Series` for 1D labelled data, `DataFrame` for 2D tabular heterogeneous data), enabling SQL-like grouping, alignment, slicing, and missing data imputation.
- **Matplotlib**: A 2D/3D graphics engine offering object-oriented plotting APIs for generating publication-ready line plots, scatter plots, bar charts, and heatmaps.
- **Scikit-learn**: The premier classical machine learning library in Python providing unified APIs (`fit`, `transform`, `predict`), preprocessing tools, pipelines, and evaluation metrics.

### 2.2 Data Structures & Complexity Reference Table

| Data Structure | Implementation Primitive | Operation | Time Complexity | Space Complexity | LIFO / FIFO / Unordered |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | Dynamic Array | Indexing `a[i]` | $O(1)$ | $O(n)$ | Ordered, Sequential |
| | | Append `a.append()` | $O(1)$ (amortized) | | |
| | | Insert / Remove `a.insert(i, x)` | $O(n)$ | | |
| **Dictionary** | Open-addressing Hash Map | Lookup `d[key]` | $O(1)$ average | $O(n)$ | Key-Value Mapping |
| | | Insert / Update `d[k] = v` | $O(1)$ average | | |
| **Set** | Hash Table | Add / Membership `x in s` | $O(1)$ average | $O(n)$ | Unordered, Unique |
| | | Union / Intersection | $O(len(s) + len(t))$ | | |
| **Stack** | List (`append`, `pop`) | Push / Pop / Peek | $O(1)$ | $O(n)$ | **LIFO** (Last In, First Out) |
| **Queue** | List (`append`, `pop(0)`) | Enqueue / Dequeue | Enqueue: $O(1)$, Dequeue: $O(n)$ | $O(n)$ | **FIFO** (First In, First Out) |
| **Optimized Queue** | `collections.deque` | Enqueue / Dequeue | Enqueue: $O(1)$, Dequeue: $O(1)$ | $O(n)$ | **FIFO** (Double-Ended Queue) |

---

## 3. Directory Structure & Source Files

```
LAB-1/
├── 01_explore_python_libraries.py   # Exploration of NumPy, Pandas, Matplotlib, Scikit-learn
├── 02_list_manipulation.py          # List operations, slicing, mutations, list comprehension
├── 03_dictionary_operations.py      # Dict lookups, nested structures, dict comprehensions
├── 04_set_properties.py             # Deduplication, set operations, vocabulary extraction
├── 05_stack_simulation.py           # OOP Stack class (LIFO), underflow check, bracket validator
├── 06_queue_simulation.py           # OOP Queue class (FIFO), underflow check, deque benchmarking
├── lib_exploration_plot.png         # Generated Matplotlib multi-panel plot
└── README.md                        # Complete lab documentation
```

---

## 4. Script Walkthroughs & Key Code Snippets

### 4.1 Script 1: `01_explore_python_libraries.py`
Demonstrates array broadcasting and model training:
```python
# NumPy vectorization and broadcasting
matrix_a = np.arange(1, 10).reshape(3, 3)
vector_b = np.array([10, 20, 30])
broadcasted_sum = matrix_a + vector_b

# Scikit-learn Logistic Regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)
```

### 4.2 Script 2: `02_list_manipulation.py`
Demonstrates slicing, sorting, and list comprehensions:
```python
# List comprehension for feature normalization [0, 1]
normalized = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]
```

### 4.3 Script 3: `03_dictionary_operations.py`
Demonstrates safe lookups and class-to-index label mapping:
```python
# Safe lookup with default fallback
grade = student_grades.get("Aditya", "N/A")

# Feature mapping via dictionary comprehension
label_to_id = {cls_name: idx for idx, cls_name in enumerate(classes)}
```

### 4.4 Script 4: `04_set_properties.py`
Demonstrates uniqueness and mathematical set algebra:
```python
# Set algebra operations
union_skills = ds_skills | web_skills         # Union
common_skills = ds_skills & web_skills        # Intersection
exclusive_ds = ds_skills - web_skills         # Difference
symmetric = ds_skills ^ web_skills            # Symmetric Difference
```

### 4.5 Script 5: `05_stack_simulation.py`
Demonstrates encapsulated LIFO behavior:
```python
class Stack:
    def __init__(self, capacity=None):
        self._items = []
        self._capacity = capacity
    def push(self, item):
        if self._capacity and len(self._items) >= self._capacity:
            raise OverflowError("Stack Overflow")
        self._items.append(item)
    def pop(self):
        if not self._items:
            raise IndexError("Stack Underflow")
        return self._items.pop()
```

### 4.6 Script 6: `06_queue_simulation.py`
Demonstrates FIFO behavior and benchmarking why `collections.deque.popleft()` ($O(1)$) outperforms `list.pop(0)` ($O(n)$):
```python
# List-based: O(n) because all remaining elements must shift left
removed = list_queue.pop(0)

# Deque-based: O(1) doubly-linked memory block pop
removed = deque_queue.popleft()
```

---

## 5. Execution Instructions
Run all scripts from the command prompt or terminal:
```bash
# Navigate to LAB-1
cd "e:\c++ dsa\DSML COLLEGE\LAB-1"

# Run individual scripts
python 01_explore_python_libraries.py
python 02_list_manipulation.py
python 03_dictionary_operations.py
python 04_set_properties.py
python 05_stack_simulation.py
python 06_queue_simulation.py
```

---

## 6. Viva & Interview Questions

1. **Why are NumPy arrays faster than standard Python lists?**
   - *Answer*: Python lists store pointers to scattered objects with dynamic type overhead. NumPy arrays allocate contiguous blocks of homogeneous memory in C/Fortran, maximizing CPU cache line locality and enabling SIMD (Single Instruction Multiple Data) vectorization.

2. **Why does `list.pop(0)` take $O(n)$ time whereas `collections.deque.popleft()` takes $O(1)$?**
   - *Answer*: Standard Python lists are flat contiguous dynamic arrays. When index 0 is deleted, all subsequent $n-1$ elements must be shifted forward by one position in memory. `collections.deque` uses a doubly linked list of fixed-size contiguous chunks, allowing pointers at both ends to be adjusted in $O(1)$ time without memory shifts.

3. **What is the difference between `.remove()` and `.pop()` in a Python list?**
   - *Answer*: `.remove(x)` searches for the first element matching value `x` and deletes it (raises `ValueError` if not present). `.pop(i)` removes and returns the element at index `i` (defaults to the last element $-1$ in $O(1)$ time).

4. **What ensures that dictionary and set lookups operate in $O(1)$ average time?**
   - *Answer*: Python dictionaries and sets use open-addressing hash tables with perturbation sequences. An element is hashed with `hash(key)`, mapping directly to a memory bucket index in constant time.
