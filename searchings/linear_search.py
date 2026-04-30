def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ---- main ----
arr = list(map(int, input('enter numbers: ').split()))
target = int(input('enter element to search: '))

result = linear_search(arr, target)

if result != -1:
    print(f'Found at index {result}')
else:
    print('Element not found')