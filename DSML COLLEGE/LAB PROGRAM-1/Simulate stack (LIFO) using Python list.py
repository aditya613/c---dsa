# Simulate Stack (LIFO) using Python list

def stack_push(stack, item):
    stack.append(item)

def stack_pop(stack):
    if len(stack) == 0:
        return "Underflow! Stack is empty"
    return stack.pop()

def stack_peek(stack):
    if len(stack) == 0:
        return "Stack is empty"
    return stack[-1]

# Demonstration
stack = ["Aditya", "Arpit", "Daksh", "Aryan"]
print("Initial Stack:", stack)

# Push
stack_push(stack, "Rohan")
print("After Push 'Rohan':", stack)

# Peek
print("Top element (Peek):", stack_peek(stack))

# Pop
print("Popped element:", stack_pop(stack))
print("Stack after Pop:", stack)
