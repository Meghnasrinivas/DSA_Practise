class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Item {item} pushed to stack")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Item {item} popped from stack")
            return item
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            print(f"Item {self.stack[-1]} peeked from stack")
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        empty = len(self.stack) == 0
        print(f"Stack is empty: {empty}")
        return empty

    def size(self):
        print(f"Size of stack: {len(self.stack)}")
        return len(self.stack)
# Example usage:
if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())  # Output: 3
    print(s.pop())   # Output: 3
    print(s.size())  # Output: 2
    print(s.is_empty())  # Output: False
    s.pop()
    s.pop()
    print(s.is_empty())  # Output: True
