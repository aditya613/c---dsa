# Simulate Queue (FIFO) using Python list

def queue_enqueue(queue, item):
    queue.append(item)

def queue_dequeue(queue):
    if len(queue) == 0:
        return "Underflow! Queue is empty"
    return queue.pop(0)

def queue_peek(queue):
    if len(queue) == 0:
        return "Queue is empty"
    return queue[0]

# Demonstration
queue = ["Aditya", "Arpit", "Aryan", "Daksh"]
print("Initial Queue:", queue)

# Enqueue
queue_enqueue(queue, "Rohan")
print("After Enqueue 'Rohan':", queue)

# Peek front
print("Front element (Peek):", queue_peek(queue))

# Dequeue
print("Dequeued element:", queue_dequeue(queue))
print("Queue after Dequeue:", queue)
