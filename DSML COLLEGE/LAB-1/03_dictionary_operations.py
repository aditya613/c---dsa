# Lab 1 - Part 3: Dictionary Operations
# 1. Create a dictionary
student = {
    "name": "Aditya",
    "roll_no": 101,
    "course": "B.Tech DSML"
}
print("Initial dictionary:", student)

# 2. Access values
print("Student Name:", student["name"])
print("Branch (using get):", student.get("branch", "Not Specified"))

# 3. Add or update key-value pair
student["marks"] = 92
student["roll_no"] = 102
print("After update:", student)

# 4. Delete a key
del student["course"]
print("After deleting 'course':", student)

# 5. Iterate through dictionary
print("\nKeys and Values:")
for key, value in student.items():
    print(f"{key}: {value}")
