
#set declaration in python
items = {10, 20, 30, 20, 40, 10}

for item in items:
    print(item)
    
items.add(50)
print("After Adding 50:", items)

# Remove an element
items.remove(20)
print("After Removing 20:", items)

print("Length of Set:", len(items))


