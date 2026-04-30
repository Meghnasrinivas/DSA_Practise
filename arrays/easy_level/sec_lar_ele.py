#second largest element in an array


def second_largest(arr):
    if len(arr) < 2:
        print('array requires atleast 2 elements')
        return None
    
    first=second=float('-inf')
    print(f'initial first = {first} second = {second}')
    for i,num in enumerate(arr):
        print(f'\niteration {i} : current number = {num}')
        if num>first:
            second=first
            first=num
            print(f'updated first to {first} second to {second}')
        elif first > num >second:
            second = num
            print(f'updated second to {num}')
        else:
            print('no update related')

    if second ==float('-inf'):
        print(f'\nno second largest element found (all elements might be same)')
        return None
    
    print(f'\nfinal result : second argest element is {second}')
    return second

arr=[4,3,55,87,2,22]
second_largest(arr)
