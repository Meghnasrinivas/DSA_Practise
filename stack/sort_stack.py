class sortStack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        if not self.stack:
            self.stack.append(data)
        else:
            while self.stack and self.stack[-1]>data:
                temp=self.stack.pop()
                self.push(data)
                self.stack.append(temp)
                return 
            self.stack.append(data)

    def pop(self):
        if not self.stack:
            print('stack is empty')
        else:
            return self.stack.pop()
        
    def peek(self):
        if not self.stack:
            print('stack is empty')
        else:
            return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack)==0
    
    def display(self):
        if not self.stack:
            print('stack is empty')
        else:
            print(self.stack)

# Example usage:
if __name__ == "__main__":
    s=sortStack()
    s.push(3)
    s.push(1)
    s.push(4)
    s.push(2)
    s.display()  # Output: [1, 2, 3, 4]
    print(s.pop())  # Output: 1
    print(s.peek())  # Output: 2
    print(s.is_empty())  # Output: False