def find_min(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[right]:
            # minimum is on right side
            left = mid + 1
        else:
            # minimum is on left side (including mid)
            right = mid
    
    return arr[left]


# ---- main ----
arr = list(map(int, input('enter rotated sorted array: ').split()))
print("Minimum element is:", find_min(arr))