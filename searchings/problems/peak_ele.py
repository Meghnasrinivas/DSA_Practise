def find_peak(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is peak
        if mid == 0:
            if arr[mid] >= arr[mid+1]:
                return mid
            else:
                left = mid + 1
        elif mid == len(arr)-1:
            if arr[mid] >= arr[mid-1]:
                return mid
            else:
                right = mid - 1
        else:
            if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                left = mid + 1   # move to right
            else:
                right = mid - 1  # move to left

# ---- main ----
arr = list(map(int, input('enter numbers: ').split()))
peak_index = find_peak(arr)
print(f'index: {peak_index}, value: {arr[peak_index]}')