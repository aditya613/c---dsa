"""
LAB 1 - Part 2.4: Simulate Stack (LIFO) Using Python List
Topics Covered:
1. Concept of Last-In-First-Out (LIFO) data structure.
2. Stack simulation using Python list primitives:
   - push() via list.append() [O(1) amortized]
   - pop() via list.pop()     [O(1)]
   - peek() / top() via list[-1] [O(1)]
   - is_empty() and size()
3. Encapsulation inside a robust, production-ready Stack class.
4. Handling Underflow conditions gracefully.
5. Real-world application: Parentheses matching / syntax validation.
"""

class Stack:
    """
    A clean, object-oriented LIFO Stack implementation backed by a Python list.
    """
    def __init__(self, capacity=None):
        self._items = []
        self._capacity = capacity

    def is_empty(self):
        """Returns True if stack contains no elements, False otherwise."""
        return len(self._items) == 0

    def size(self):
        """Returns the current number of elements in the stack."""
        return len(self._items)

    def push(self, item):
        """
        Pushes an element onto the top of the stack.
        Raises OverflowError if bounded capacity is exceeded.
        """
        if self._capacity is not None and len(self._items) >= self._capacity:
            raise OverflowError(f"Stack Overflow! Capacity of {self._capacity} reached.")
        self._items.append(item)
        print(f"[PUSH] Inserted '{item}' -> Stack now: {self._items}")

    def pop(self):
        """
        Removes and returns the top element of the stack (LIFO).
        Raises IndexError if the stack is empty (Underflow).
        """
        if self.is_empty():
            raise IndexError("Stack Underflow! Cannot pop from an empty stack.")
        removed = self._items.pop()
        print(f"[POP]  Removed '{removed}' -> Stack now: {self._items}")
        return removed

    def peek(self):
        """
        Inspects and returns the top element without removing it.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek failed! Stack is empty.")
        return self._items[-1]

    def display(self):
        """Displays the stack contents with the top clearly marked."""
        if self.is_empty():
            print("Stack: [EMPTY]")
        else:
            print(f"Stack: {self._items} <- [TOP: {self._items[-1]}]")


def check_balanced_parentheses(expression):
    """
    Practical Computer Science Application:
    Validates balanced parentheses/brackets using the Stack class.
    """
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in mapping.values():
            stack.push(char)
        elif char in mapping.keys():
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    print("=" * 80)
    print("LAB 1 - PART 2.4: STACK (LIFO) SIMULATION")
    print("=" * 80)

    # Instantiate stack with maximum capacity of 5
    my_stack = Stack(capacity=5)
    print("Created an empty Stack with capacity = 5")
    print(f"Is stack empty? {my_stack.is_empty()}")

    # Push operations
    print("\n--- Performing Push Operations ---")
    my_stack.push("Page A: Home")
    my_stack.push("Page B: Products")
    my_stack.push("Page C: Product Details")
    my_stack.push("Page D: Checkout")
    my_stack.display()

    # Peek operation
    print(f"\nCurrent Top Element (Peek): {my_stack.peek()}")

    # Pop operations (Simulating Browser 'Back' button)
    print("\n--- Performing Pop Operations (LIFO) ---")
    my_stack.pop()
    my_stack.pop()
    my_stack.display()

    print(f"\nCurrent Stack Size: {my_stack.size()}")
    print(f"Is stack empty? {my_stack.is_empty()}")

    # Test Stack Underflow Guard
    print("\n--- Testing Underflow Handling ---")
    my_stack.pop()
    my_stack.pop()
    my_stack.display()

    try:
        my_stack.pop()
    except IndexError as e:
        print(f"Caught expected Underflow exception: {e}")

    # Application: Balanced Parentheses
    print("\n--- Real-World Application: Expression Syntax Validation ---")
    test_expr1 = "{[a + b] * (c - d)}"
    test_expr2 = "{[a + b] * (c - d)"
    print(f"Expression: '{test_expr1}' -> Balanced? {check_balanced_parentheses(test_expr1)}")
    print(f"Expression: '{test_expr2}' -> Balanced? {check_balanced_parentheses(test_expr2)}")
    print("=" * 80)
