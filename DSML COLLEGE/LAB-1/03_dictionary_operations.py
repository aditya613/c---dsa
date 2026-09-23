"""
LAB 1 - Part 2.2: Use a Dictionary to Store and Retrieve Key-Value Pairs
Topics Covered:
1. Dictionary initialization and key-value semantics.
2. Direct key lookup vs safe lookup with get(key, default).
3. Modifying existing entries and dynamically adding new pairs.
4. Built-in methods: keys(), values(), items(), pop(), update().
5. Iterating through dictionaries (keys, values, unpacked items).
6. Nested dictionaries modeling complex hierarchical records (student/ML metadata).
7. Dictionary comprehensions for feature inversion / label mapping.
"""

print("=" * 80)
print("LAB 1 - PART 2.2: DICTIONARY OPERATIONS IN PYTHON")
print("=" * 80)

# 1. Dictionary Creation
student_grades = {
    "Aditya": "A+",
    "Aarav": "A",
    "Diya": "A+",
    "Kabir": "B",
    "Meera": "A"
}
print(f"Initial Dictionary: {student_grades}")
print(f"Total Entries: {len(student_grades)}")

# 2. Key Access & Retrieval
print("\n--- Key Retrieval ---")
print(f"Direct Lookup (student_grades['Aditya']): {student_grades['Aditya']}")

# Safe access with get()
print(f"Safe Lookup existing (get('Diya')): {student_grades.get('Diya')}")
print(f"Safe Lookup missing (get('Rohan', 'Not Found')): {student_grades.get('Rohan', 'Not Found')}")

# 3. Insertion and Mutation
print("\n--- Insertion and Mutation ---")
student_grades["Rohan"] = "B+"         # Add new key-value pair
student_grades["Kabir"] = "A-"         # Update existing key
print(f"After updates: {student_grades}")

# Bulk update with another dictionary
student_grades.update({"Simran": "O", "Tanmay": "B"})
print(f"After bulk update(): {student_grades}")

# 4. Deleting Elements
print("\n--- Deletion Methods ---")
removed_val = student_grades.pop("Tanmay")
print(f"Removed 'Tanmay' with grade '{removed_val}' using pop()")
del student_grades["Rohan"]
print(f"Removed 'Rohan' using del: {student_grades}")

# 5. Iterating Over Dictionaries
print("\n--- Dictionary Iteration ---")
print("All Keys:", list(student_grades.keys()))
print("All Values:", list(student_grades.values()))

print("\nIterating through key-value pairs (items()):")
for student, grade in student_grades.items():
    print(f" - Student: {student:<10} | Grade: {grade}")

# 6. Nested Dictionary: Complex ML Metadata Structure
print("\n--- Nested Dictionary (ML Model Configuration) ---")
model_config = {
    "model_name": "RandomForestClassifier",
    "hyperparameters": {
        "n_estimators": 100,
        "max_depth": 10,
        "criterion": "gini",
        "random_state": 42
    },
    "metrics": {
        "train_accuracy": 0.985,
        "test_accuracy": 0.942,
        "f1_score": 0.938
    }
}

print(f"Model: {model_config['model_name']}")
print(f"Hyperparameter n_estimators: {model_config['hyperparameters']['n_estimators']}")
print(f"Test Accuracy: {model_config['metrics']['test_accuracy'] * 100:.2f}%")

# 7. Dictionary Comprehension (Label Encoding Map)
print("\n--- Dictionary Comprehension (Feature/Label Mapping) ---")
classes = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
label_to_id = {cls_name: idx for idx, cls_name in enumerate(classes)}
id_to_label = {idx: cls_name for cls_name, idx in label_to_id.items()}

print(f"Class to ID mapping: {label_to_id}")
print(f"ID to Class mapping: {id_to_label}")
print("=" * 80)
