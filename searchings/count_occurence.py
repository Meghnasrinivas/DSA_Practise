#count occurence

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

def last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            left = mid + 1   # move right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans

def count_occurrence(nums, target):
    first_index = first_occurrence(nums, target)
    last_index = last_occurrence(nums, target)

    if first_index == -1 or last_index == -1:
        return 0  # Element not found

    return last_index - first_index + 1

nums = list(map(int, input('enter only sorted numbers: ').split()))

# 🚫 Block if not sorted
if not is_sorted(nums):
    print("❌ Array is not sorted. Please enter sorted array.")
else:
    target = int(input('enter element to be searched: '))
    
    result = count_occurrence(nums, target)
    
    if result != 0:
        print(f"Element found {result} times.")
    else:
        print("Element not found")