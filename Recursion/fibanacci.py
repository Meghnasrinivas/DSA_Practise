# Fibonacci Using Recursion (Interview Friendly)

def fibanacci(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    return fibanacci(n-1) +fibanacci(n-2)
n=int(input())
print(fibanacci(n))