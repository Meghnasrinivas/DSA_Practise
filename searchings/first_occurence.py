# fist occurence

def is_sorted(nums):
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

def first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            right = mid - 1   # move left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans

nums = list(map(int, input('enter only sorted numbers: ').split()))

# 🚫 Block if not sorted
if not is_sorted(nums):
    print("❌ Array is not sorted. Please enter sorted array.")
else:
    target = int(input('enter fist element to be searched: '))
    
    result = first_occurrence(nums, target)
    
    if result != -1:
        print(f"first occurence Found at index {result} and target is {nums[result]}")
    else:
        print("Element not found")