# palindrome

def is_palindrome(s):
    # Base case
    if len(s) <= 1:
        return True
    
    # Check first and last characters
    if s[0] != s[-1]:
        return False
    
    # Recursive call on substring excluding first and last char
    return is_palindrome(s[1:-1])


# Example
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False