#reverse a str

def reverse_str(s):
    return s[::-1]
user = input('enter a string : ')
reversed=reverse_str(user)
print(f'reversed string is : {reversed}')

#reverse  words
s1='i love code'.split()
print(' '.join(s1[::-1]))