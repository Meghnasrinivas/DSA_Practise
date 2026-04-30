#Sort an Array

def sort(nums):
    for i in range(0,len(nums)):
        nums.sort()
        return nums
    
nums = list(map(int,input('enter numbers to be sorted :').split()))
print(sort(nums))