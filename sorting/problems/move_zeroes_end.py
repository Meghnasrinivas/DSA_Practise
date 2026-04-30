# move all zeroes to end

def move_zeroes(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    while count < len(nums):
        nums[count] = 0
        count += 1
    return nums

nums = list(map(int,input('enter numbers to be sorted :').split()))
print(move_zeroes(nums))