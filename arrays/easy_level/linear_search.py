#linear search

def linear_search(arr,target):
    attempt=0
    print(f'initial array {arr}\ntargeted element is {target}')
    for i,num in enumerate((arr)):
        if num == target:
            print(f'element found at arr[{i}] and the element is {num} in attempt number {attempt}')
            return i
        else:
            print(f'element not found... at arr[{i}]')
            attempt+=1
linear_search([2,3,4,5,6,7],6)
