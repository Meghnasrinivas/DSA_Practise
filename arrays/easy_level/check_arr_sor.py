 #check if array is sorted

def is_sorted(arr):
    if len(arr) < 2:
        print(f'for array containing less than 2 elements , sorted by default')
        return True
    
    print(f'checking array : {arr}')
    for i in range(1,len(arr)):
        print(f'iteration {i} :\narr[{i-1}] = {arr[i-1]} , arr[{i}] = {arr[i]}')
        if arr[i] > arr[i-1] :
            print(f'array is sorted\n')
            # return True
        else:
            print(f'found a decrease -array is NOT in sorted order\n')

    print('No violations found -array is sorted\n')
    return True

arr=[-3,4,9,1,3]
is_sorted(arr)