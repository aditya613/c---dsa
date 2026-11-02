# Lab 1 - Part 5: Stack Simulation (LIFO - Last In, First Out)
stack = []

# Push elements onto stack
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)

# Peek top element
if len(stack) > 0:
    print("Top element (peek):", stack[-1])

# Pop elements from stack
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Stack now:", stack)

# Check if empty
print("Is stack empty?", len(stack) == 0)
