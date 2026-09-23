"""
LAB 1 - Part 2.5: Simulate Queue (FIFO) Using Python List
Topics Covered:
1. Concept of First-In-First-Out (FIFO) data structure.
2. Queue simulation using Python list primitives:
   - enqueue() via list.append() [O(1)]
   - dequeue() via list.pop(0)    [O(n) due to element shifting]
   - front() via list[0]          [O(1)]
   - is_empty() and size()
3. Performance trade-off analysis: Why list.pop(0) is O(n) vs collections.deque O(1).
4. Dual implementation: List-based Queue vs Collections.deque Queue.
5. Real-world application: Customer Service / Batch Job Scheduling.
"""

from collections import deque
import time

class ListQueue:
    """
    FIFO Queue implementation using a standard Python list.
    Demonstrates fundamental queue mechanics and underflow handling.
    """
    def __init__(self):
        self._queue = []

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return len(self._queue) == 0

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self._queue)

    def enqueue(self, item):
        """Adds an item to the rear of the queue (FIFO)."""
        self._queue.append(item)
        print(f"[ENQUEUE] Added '{item}' to rear -> Queue: {self._queue}")

    def dequeue(self):
        """
        Removes and returns the front item of the queue (FIFO).
        Raises IndexError if the queue is empty (Underflow).
        Note: list.pop(0) takes O(n) time because remaining elements shift left.
        """
        if self.is_empty():
            raise IndexError("Queue Underflow! Cannot dequeue from an empty queue.")
        removed = self._queue.pop(0)
        print(f"[DEQUEUE] Removed '{removed}' from front -> Queue: {self._queue}")
        return removed

    def front(self):
        """Inspects the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! No front element.")
        return self._queue[0]

    def display(self):
        """Displays the entire queue with Front and Rear markers."""
        if self.is_empty():
            print("Queue: [EMPTY]")
        else:
            print(f"Queue: [FRONT] {self._queue} [REAR]")


class DequeQueue:
    """
    High-performance FIFO Queue using collections.deque.
    Provides strictly O(1) time complexity for both append and popleft.
    """
    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if not self._queue:
            raise IndexError("Queue is empty.")
        return self._queue.popleft()

    def size(self):
        return len(self._queue)


if __name__ == "__main__":
    print("=" * 80)
    print("LAB 1 - PART 2.5: QUEUE (FIFO) SIMULATION")
    print("=" * 80)

    # 1. Basic Queue Operations
    q = ListQueue()
    print("Instantiated an empty ListQueue.")
    print(f"Is queue empty? {q.is_empty()}")

    # Enqueue elements (e.g. print jobs)
    print("\n--- Enqueue Operations ---")
    q.enqueue("Job_101: ML_Report.pdf")
    q.enqueue("Job_102: Model_Weights.bin")
    q.enqueue("Job_103: Plots.png")
    q.enqueue("Job_104: Syllabus.docx")
    q.display()

    # Front inspection
    print(f"\nFront element waiting for service: {q.front()}")

    # Dequeue elements (FIFO order: Job 101 serviced first)
    print("\n--- Dequeue Operations (FIFO Service) ---")
    q.dequeue()
    q.dequeue()
    q.display()

    print(f"\nCurrent Queue Size: {q.size()}")

    # Clear remaining
    print("\n--- Clearing Queue & Testing Underflow ---")
    q.dequeue()
    q.dequeue()
    q.display()

    try:
        q.dequeue()
    except IndexError as e:
        print(f"Caught expected Underflow exception: {e}")

    # 2. Performance Comparison: Python List vs collections.deque
    print("\n--- Complexity Analysis: List vs collections.deque for 20,000 Dequeues ---")
    n_ops = 20000

    # List queue benchmark
    list_q = list(range(n_ops))
    start_time = time.time()
    for _ in range(n_ops):
        list_q.pop(0)
    list_time = time.time() - start_time
    print(f"Python list.pop(0) [O(n) per pop] time:       {list_time:.4f} seconds")

    # Deque benchmark
    deq_q = deque(range(n_ops))
    start_time = time.time()
    for _ in range(n_ops):
        deq_q.popleft()
    deq_time = time.time() - start_time
    print(f"collections.deque.popleft() [O(1) per pop] time: {deq_time:.4f} seconds")

    speedup = list_time / deq_time if deq_time > 0 else float('inf')
    print(f"collections.deque was {speedup:.1f}x faster for high-throughput queues!")
    print("=" * 80)
