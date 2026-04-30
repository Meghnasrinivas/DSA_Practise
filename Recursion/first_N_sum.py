 # sum of First N Numbers Using Recursion

def sum(n):
    if n<=0:
        return 0
    return n+sum(n-1)
n=int(input())
print(sum(n))