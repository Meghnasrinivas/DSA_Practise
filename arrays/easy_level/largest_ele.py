#Arrays practise from take u forward
#Easy level
#1.largest element in an array


def  find_largest(arr):
    if not arr:
        return None #handles empty array
    max_number=arr[0]
    print(f'initialy maximum number : {max_number}')

    for i in range(1,len(arr)) :
        print(f'comparing current max = {max_number} with arr[{i}] = {arr[i]}')
        if arr[i] > max_number :
                max_number = arr[i]
                print(f'updated maximum number to {max_number}')  
        else:
                print('No updation needed')

    print(f'\nfinal largest element : {max_number}')
    return max_number

arr=[3,5,2,9,1,2]
find_largest(arr)

