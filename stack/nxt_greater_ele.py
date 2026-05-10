class NextGreaterElement:
    def __init__(self,arr):
        self.arr=arr
        self.stack=[]
        self.result=[-1]*len(arr)

    def find_next_greater(self):
        for i in range(len(self.arr)):
            while self.stack and self.arr[self.stack[-1]]<self.arr[i]:
                index=self.stack.pop()
                self.result[index]=self.arr[i]
            self.stack.append(i)
        return self.result
    
# Example usage:
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    nge = NextGreaterElement(arr)
    print(nge.find_next_greater())  # Output: [5, 10, 10, -1, -1]
