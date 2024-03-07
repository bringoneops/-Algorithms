class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Initialize an empty stack

    def push(self, value):
        new_node = Node(value)  # Create a new node with the given value
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node  # Update the head to the new node

    def pop(self):
        if self.is_empty():
            raise Exception("Pop from an empty stack")  # Handle empty stack case
        pop_value = self.head.value  # Retrieve the value to pop
        self.head = self.head.next  # Update the head to the next node, effectively removing the top node
        return pop_value

    def is_empty(self):
        return self.head is None  # Stack is empty if head is None

# Testing the stack implementation
stack = Stack()
stack.push(10)
stack.push(30)
print(f"POP: {stack.pop()}")  # Expected to pop 30
stack.push(80)
print(f"POP: {stack.pop()}")  # Expected to pop 80
