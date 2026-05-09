class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def empty(self):
        return self.top is None
    
    def push(self,data):
        self.new_node=Node(data)
        self.new_node.next=self.top
        self.top=self.new_node
        print(f'pushed {data}')

    def pop(self):
        if self.empty():
            print('stack underflow!! u canot pop from an empty stack')
            return None
        self.popped_node=self.top
        self.top=self.top.next
        print(f'popped {self.popped_node.data}')
        return self.popped_node.data
    
    def peek(self):
        if self.empty():
            print('stack underflow!! u canot get top from an empty stack')
            return None
        print(f'top element {self.top.data}')

    def display(self):
        if self.empty():
            print('stack underflow!! u canot get elements from an empty stack')
            return None
        self.current=self.top
        print('stack (top to bottom)',end=' ')
        while self.current:
            print(self.current.data , end='-->')
            self.current=self.current.next
        print('None')

stack=Stack()
stack.push(3)
stack.push(30)
stack.push(300)
stack.peek()
stack.display()
stack.pop()
stack.pop()
stack.display()
stack.pop()
stack.push(4)
stack.push(90)
stack.display()
stack.peek()


