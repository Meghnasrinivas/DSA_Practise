## left rotate array by d places

def reverse(arr,start,end):
    while start<end:
        arr[start] , arr[end] =arr[end], arr [start]
        start+=1
        end-=1

def left_rotate(arr , d):
    n=len(arr)
    d= d % n

    reverse(arr , 0,d-1)
    reverse(arr , d,n-1)
    reverse(arr , 0,n-1)
    return arr

arr=[1,2,3,4,5]
print(left_rotate(arr,2))
