class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    # Enqueue
    def enqueue(self, data):

        # queue full
        if self.rear == self.size - 1:
            print("queue overflow")
            return

        # first insertion
        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = data

        print(f"{data} inserted")

    # Dequeue
    def dequeue(self):

        # queue empty
        if self.front == -1 or self.front > self.rear:
            print("queue underflow")
            return None

        removed = self.queue[self.front]
        self.front += 1

        return removed

    # Front element
    def peek_front(self):
        if self.front == -1 or self.front > self.rear:
            print("queue empty")
            return None

        return self.queue[self.front]

    # Rear element
    def peek_rear(self):
        if self.front == -1 or self.front > self.rear:
            print("queue empty")
            return None

        return self.queue[self.rear]

    # Display
    def display(self):

        if self.front == -1 or self.front > self.rear:
            print("queue empty")
            return

        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")

        print()


# Example
q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("front:", q.peek_front())
print("rear:", q.peek_rear())

print("deleted:", q.dequeue())

q.display()