#Check if an Array is Sorted

def check_sort(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True
nums = list(map(int,input('enter numbers to be sorted :').split()))
print(check_sort(nums))