class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.queue = []

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return an item from the front of the queue
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def print_queue(self):
        # Print all items in the queue
        print("Queue:", self.queue)

if __name__ == "__main__":
    # Create an instance of Queue
    queue = Queue()
    # Add items to the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Original queue:")
    # Print the original queue
    queue.print_queue()
    # Remove an item from the queue
    queue.dequeue()
    print("Queue after dequeuing an element:")
    # Print the queue after dequeuing an element
    queue.print_queue()