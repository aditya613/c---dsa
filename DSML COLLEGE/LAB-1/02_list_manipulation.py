"""
LAB 1 - Part 2.1: Practice Basic List Manipulation Commands in Python
Topics Covered:
1. List declaration, indexing (positive/negative), and slicing [start:stop:step].
2. Adding elements: append(), insert(), extend(), concatenation.
3. Removing elements: remove(), pop(), del, clear().
4. Searching and counting: in operator, index(), count().
5. Ordering & transformation: sort(reverse=True/False), sorted(), reverse().
6. List comprehension for mathematical transformations and filtering.
"""

print("=" * 80)
print("LAB 1 - PART 2.1: LIST MANIPULATION IN PYTHON")
print("=" * 80)

# 1. Declaration and Basic Properties
students = ["Aditya", "Arpit", "Aryan", "Daksh", "Navneet"]
print(f"Initial Students List: {students}")
print(f"List Length: {len(students)}")
print(f"First element (students[0]): {students[0]}")
print(f"Last element (students[-1]): {students[-1]}")
print(f"Sub-list slice (students[1:4]): {students[1:4]}")
print(f"Reversed slice (students[::-1]): {students[::-1]}")

# 2. Modifying Elements (Mutability)
print("\n--- Modifying Elements ---")
students[0] = "Ankush"
print(f"After students[0] = 'Ankush': {students}")

# 3. Adding Elements
print("\n--- Adding Elements ---")
students.append("Rohan")             # Add to end
print(f"After append('Rohan'): {students}")

students.insert(2, "Manvi")          # Insert at index 2
print(f"After insert(2, 'Manvi'): {students}")

new_joiners = ["Simran", "Tanmay"]
students.extend(new_joiners)         # Extend with another iterable
print(f"After extend(['Simran', 'Tanmay']): {students}")

# 4. Removing Elements
print("\n--- Removing Elements ---")
students.remove("Arpit")             # Remove first occurrence of value
print(f"After remove('Arpit'): {students}")

popped_item = students.pop()         # Remove and return last element
print(f"After pop() [popped '{popped_item}']: {students}")

popped_index = students.pop(1)       # Remove item at specific index
print(f"After pop(1) [popped '{popped_index}']: {students}")

del students[0]                      # del statement
print(f"After del students[0]: {students}")

# 5. Searching and Counting
print("\n--- Searching and Counting ---")
target = "Manvi"
if target in students:
    idx = students.index(target)
    print(f"'{target}' is found at index {idx}")

students.append("Daksh")             # Duplicate element for count demonstration
print(f"Current list with duplicate: {students}")
print(f"Count of 'Daksh': {students.count('Daksh')}")

# 6. Sorting and Reversing
print("\n--- Sorting and Reversing ---")
# in-place sort
students.sort()
print(f"In-place Ascending sort(): {students}")

students.sort(reverse=True)
print(f"In-place Descending sort(reverse=True): {students}")

# Non-mutating sorted()
scores = [88, 45, 92, 76, 64, 99, 81]
sorted_scores = sorted(scores)
print(f"Original Scores: {scores}")
print(f"Sorted Scores (new list): {sorted_scores}")

# 7. List Comprehension (Pythonic power tool for ML data preprocessing)
print("\n--- List Comprehensions ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in numbers]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
normalized_0_1 = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]

print(f"Original numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Even Squares: {even_squares}")
print(f"Normalized [0, 1] features: {[round(n, 2) for n in normalized_0_1]}")
print("=" * 80)
