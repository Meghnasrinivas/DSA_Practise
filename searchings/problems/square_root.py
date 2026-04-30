#  square root using binary search

def sqrt_root(x):
    if x == 0 or x == 1:
        return x
    
    left, right = 0, x
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid   # store last valid mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans


# ---- main ----
x = int(input('Enter number to find square root: '))
print(f'Square root of given number is {sqrt_root(x)}')