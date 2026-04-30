 #move al zeros to end of array

def move_zeroes(arr):
    non_zero_index=0
    print(f'checking array : {arr}')
    for i in range(len(arr)):
        if arr[i] !=0:
            arr[non_zero_index],arr[i] = arr[i] ,arr[non_zero_index]
            non_zero_index +=1
        print('array after each iteration' , arr)
    return arr
        
arr=[0,5,3,0,5,0]
print(move_zeroes(arr))
