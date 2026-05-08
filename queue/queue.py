class queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        empty = len(self.items) == 0
        print(f"Queue is empty: {empty}")    
        return empty

    def enqueue(self, item):
        self.items.insert(0, item)
        print(f"Item {item} enqueued to queue")
    
    def dequeue(self):
        item = self.items.pop()
        print(f"Item {item} dequeued from queue")
        return item
    
    def size(self):
        size = len(self.items)
        print(f"Size of queue: {size}")
        return size

# Example usage:
if __name__ == "__main__":
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Output: 1
    print(q.size())     # Output: 2
    print(q.isEmpty())  # Output: False
    q.dequeue()
    q.dequeue()
    print(q.isEmpty())  # Output: True