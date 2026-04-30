# Count Number of Digits Using Recursion

def count_digits(n):
    n=abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
number = 12345
print("The number of digits in", number, "is", count_digits(number))