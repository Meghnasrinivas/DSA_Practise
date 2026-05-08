from array import*

class StackUsingArrays:
    def __init__(self,size):
        self.size=size
        self.top=-1
        self.arr=array('i',[])
    
    def push(self,data):
        if self.top==self.size-1:
            print("stack overflow")
        else:
            self.top+=1
            self.arr.append(data)
    
    def pop(self):
        if self.top==-1:
            print()
            print("stack underflow")
        else:
            self.arr.pop()
            self.top-=1
    
    def peek(self):
        if self.top==-1:
            print("stack is empty")
        else:
            return self.arr[self.top]
    
    def display(self):
        for i in range(self.top,-1,-1):
            print(self.arr[i],end=" ")
# Example usage:
if __name__ == "__main__":
    stack = StackUsingArrays(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())  # Output: 3
    stack.pop()
    print(stack.peek())  # Output: 2 
    stack.display()  # Output: 2 1
    stack.pop()
    stack.pop()
    stack.pop()  # Output: stack underflow
