from collections import deque

class Queue: 
    def __init__(self):
        self.queue = deque()

    def __init__(self, item):  
        self.queue.append(item)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
    def is_empty(self):
        return len(self.queue) == 0 