# palindrome
def is_palindrome(s):
    if s==s[::-1]:
        return True
    return False
user = input('enter a string : ')
print(f'is palindrome : {is_palindrome(user)}')