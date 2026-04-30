# Factorial Using Recursion

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
fact=int(input('enter a number to find factorial : '))
print(f"factorial of {fact} is : {factorial(fact)}")