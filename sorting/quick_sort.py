#quick sort

def partition(arr,lb,ub):
    pivot=arr[lb]
    start=lb
    end=ub


    while start<end:
        while arr[start]<=pivot and start < ub:
            start+=1
        while arr[end]>=pivot and end>lb :
            end-=1
        if start< end:
           arr[start],arr[end]=arr[end],arr[start]
    arr[lb], arr[end] = arr[end], arr[lb]
    return end


def quick_sort(arr,lb,ub):
    if lb<ub:
        lock=partition(arr,lb,ub)
        quick_sort(arr,lb,lock-1)
        quick_sort(arr,lock+1,ub)


arr=[4,56,20,1,0,7,54,24]
print('unsorted array : ',arr)
quick_sort(arr,0,len(arr)-1)
print('sorted array : ',arr)