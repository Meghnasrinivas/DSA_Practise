# Binary Search

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return -1


arr = list(map(int, input('enter only sorted numbers: ').split()))

# 🚫 Block if not sorted
if not is_sorted(arr):
    print("❌ Array is not sorted. Please enter sorted array.")
else:
    target = int(input('enter element to be searched: '))
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Found at index {result} and target is {arr[result]}")
    else:
        print("Element not found")