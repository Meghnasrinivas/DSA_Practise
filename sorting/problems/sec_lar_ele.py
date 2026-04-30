# Find 2nd Largest Element

def second_largest(nums):
    nums=list(set(nums))

    if len(nums)<2:
        return 'there is no second largest element'
    
    nums.sort()
    return nums[-2]
    
nums = list(map(int,input('enter numbers to be sorted :').split()))
print(second_largest(nums))