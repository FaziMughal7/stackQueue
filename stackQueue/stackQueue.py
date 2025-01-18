class Node:
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.next = None  # Initialize the next pointer to None

class Stack:
    def __init__(self):
        self.top = None  # Initialize the stack as empty

    def add(self, value):
        """Push a value onto the stack."""
        new_node = Node(value)  # Create a new node
        new_node.next = self.top  # Point the new node's next to the current top
        self.top = new_node  # Update the top to the new node

    def remove(self):
        """Pop a value from the stack."""
        if self.top:  # If the stack is not empty
            removed = self.top.value  # Get the top value
            self.top = self.top.next  # Move the top pointer to the next node
            return f"Removed: {removed}"
        return "Stack is empty!"  # Return if the stack is empty

    def peek(self):
        """Return the top value of the stack."""
        return f"Top value: {self.top.value}" if self.top else "Stack is empty!"  # Return the top value or empty message

    def show(self):
        """Display the elements in the stack."""
        current = self.top
        stack_elements = []  # List to store stack elements for display
        while current:
            stack_elements.append(str(current.value))  # Add current value to the list
            current = current.next  # Move to the next node
        return " -> ".join(stack_elements) + " -> None"  # Return the stack elements as a string

class Queue:
    def __init__(self):
        self.front = self.rear = None  # Initialize the queue as empty

    def add(self, value):
        """Enqueue a value to the queue."""
        new_node = Node(value)  # Create a new node
        if not self.rear:  # If the queue is empty
            self.front = self.rear = new_node  # Set both front and rear to the new node
        else:
            self.rear.next = new_node  # Link the new node after the rear
            self.rear = new_node  # Move the rear pointer to the new node

    def remove(self):
        """Dequeue a value from the queue."""
        if self.front:  # If the queue is not empty
            removed = self.front.value  # Get the front value
            self.front = self.front.next  # Move the front pointer to the next node
            if not self.front: self.rear = None  # If the queue is empty, reset the rear to None
            return f"Removed: {removed}"
        return "Queue is empty!"  # Return if the queue is empty

    def peek(self):
        """Return the front value of the queue."""
        return f"Front value: {self.front.value}" if self.front else "Queue is empty!"  # Return the front value or empty message

    def show(self):
        """Display the elements in the queue."""
        current = self.front
        queue_elements = []  # List to store queue elements for display
        while current:
            queue_elements.append(str(current.value))  # Add current value to the list
            current = current.next  # Move to the next node
        return " -> ".join(queue_elements) + " -> None"  # Return the queue elements as a string

# Testing Stack and Queue
if __name__ == "__main__":
    # Stack operations
    stack = Stack()
    stack.add(5)  # Add elements to the stack
    stack.add(10)
    stack.add(15)
    print(stack.show())  # Show stack contents
    print(stack.remove())  # Remove top element from stack
    print(stack.peek())  # Peek at top element
    print(stack.show())  # Show stack contents after removal

    # Queue operations
    queue = Queue()
    queue.add(3)  # Add elements to the queue
    queue.add(2)
    queue.add(1)
    print(queue.show())  # Show queue contents
    print(queue.remove())  # Remove front element from queue
    print(queue.peek())  # Peek at front element
    print(queue.show())  # Show queue contents after removal

