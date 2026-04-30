# Remove duplicates from array

def remove_duplicates(nums):
    nums=list(set(nums))
    nums.sort()
    return nums
nums = list(map(int,input('enter numbers to be sorted :').split()))
print(remove_duplicates(nums))