from collections import deque

# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            dequeued = self.queue.popleft()
            print(f"Dequeued: {dequeued}")
            return dequeued
        raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Sample Usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')

    print(f"Front element is: {q.peek()}")
    q.dequeue()
    print(f"Is queue empty? {q.is_empty()}")
    print(f"Queue size: {q.size()}")
