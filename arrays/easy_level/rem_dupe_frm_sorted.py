#remove duplicates from sorted array

def remove_duplicate(arr):
    if not arr:
        return 0
    write_index=1

    print(f'initial array {arr}')
    for read_index in range(1,len(arr)):
        if arr[read_index]!= arr[write_index - 1]:
            arr[write_index]=arr[read_index]
            print(f'unique found ,placing arr[{read_index}] --> arr[{write_index}] : {arr}')
            write_index+=1
        else: 
            print(f'found dupicate , skipping....')
    print(f'final array (no duplicate {arr[:write_index]})')
    print(f'final array (with duplicate) {arr[write_index:]}')
    return arr

arr=[1,1,2,2,2,3,3]
remove_duplicate(arr)

