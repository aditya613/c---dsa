# Lab 1 - Part 6: Queue Simulation (FIFO - First In, First Out)
queue = []

# Enqueue (Insert at rear)
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")
print("Queue after enqueues:", queue)

# Peek front element
if len(queue) > 0:
    print("Front element:", queue[0])

# Dequeue (Remove from front)
print("Dequeued:", queue.pop(0))
print("Dequeued:", queue.pop(0))
print("Queue now:", queue)

# Check if empty
print("Is queue empty?", len(queue) == 0)
