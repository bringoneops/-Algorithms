class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Start of the queue
        self.rear = None   # End of the queue

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        dequeue_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeue_value

# Testing the queue implementation
queue = Queue()
queue.enqueue(4)
queue.enqueue(1)
queue.enqueue(3)
print(f"DEQUEUE: {queue.dequeue()}")  # Expected to dequeue 4
queue.enqueue(8)
print(f"DEQUEUE: {queue.dequeue()}")  # Expected to dequeue 1
