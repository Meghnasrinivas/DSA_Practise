#left rotate array bt one place


def rotate_left_byOne(arr):
    n=len(arr)
    if n==0:
        return f'cannot perform as array is 0'
    
    print('Initial array : ',arr)
    store_first_ele=arr[0]
    print(f'sorted first element {store_first_ele}')
    
    for i in range(1,n):
        arr[i-1]=arr[i]
        print(f'after moving arr[{i}] to arr[{i-1}] : {arr}')
    arr[n-1]= store_first_ele
    print(f'final array after rotating to left {arr}')
    return arr
arr=[1,2,3,4,5]
rotate_left_byOne(arr)

