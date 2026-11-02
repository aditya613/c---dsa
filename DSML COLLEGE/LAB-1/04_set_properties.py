# Lab 1 - Part 4: Set Operations
# 1. Sets store unique, unordered elements
nums = {1, 2, 2, 3, 4, 4, 5}
print("Set (duplicates removed automatically):", nums)

# 2. Add and Remove
nums.add(6)
nums.remove(1)
print("After add(6) and remove(1):", nums)

# 3. Mathematical Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union (A | B):", set_a | set_b)
print("Intersection (A & B):", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
