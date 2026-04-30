# Revese a sting using Recursion

def reverse_string(s):
    # Base case
    if len(s) <= 1:
        return s
    
    # Recursive case
    return reverse_string(s[1:]) + s[0]


# Example
print(reverse_string("meghana"))