#maximum consecutive one's

def max_consective_one(arr):
    max_count = 0
    current_count = 0
    print(f'\n initialy array {arr}')
    for i ,num in enumerate(arr):
        print(f'arr {i} = {num}')
        if num == 1:
            current_count+=1
            print(f'found 1 ==> current streak {current_count}')
        else:
            print(f'found a 0 time to reset current count streak')
            current_count=0
            print(f'current streak reset to {current_count}')
        
        if current_count > max_count:
          max_count =current_count
          print(f'updated max_count to {max_count}')

        print()

    print(f'maximum consecutive count {max_count}')
    return max_count
max_consective_one([1,1,0,1,1,1,1])
