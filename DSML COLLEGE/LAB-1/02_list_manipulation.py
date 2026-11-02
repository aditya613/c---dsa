# Lab 1 - Part 2: List Operations
# 1. Create a list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# 2. Append (Add at end)
fruits.append("orange")
print("After append:", fruits)

# 3. Insert at specific index
fruits.insert(1, "mango")
print("After insert at index 1:", fruits)

# 4. Remove by value
fruits.remove("banana")
print("After remove 'banana':", fruits)

# 5. Pop by index (removes and returns element)
popped_item = fruits.pop()
print(f"Popped '{popped_item}', List now:", fruits)

# 6. Slicing
print("Slice [0:2]:", fruits[0:2])

# 7. Sorting
fruits.sort()
print("After sorting:", fruits)
