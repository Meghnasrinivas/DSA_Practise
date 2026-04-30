#insertion sort


def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
        
arr=[4,8,1,3,9,0]
print('unsorted array ; ',arr)
insertion_sort(arr)
print('sorted array ',arr)
