#   Search Insert Position


def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def search_insert(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1

    return left  # Return the insertion point

arr = list(map(int, input('enter only sorted numbers: ').split()))

# 🚫 Block if not sorted
if not is_sorted(arr):
    print("❌ Array is not sorted. Please enter sorted array.")
else:
    target = int(input('enter element to be searched: '))
    
    result = search_insert(arr, target)
    
    # 🔥 No "not found" case now
    if result < len(arr) and arr[result] == target:
        print(f"Found at index {result}")
    else:
        print(f"Not found. Can be inserted at index {result}")