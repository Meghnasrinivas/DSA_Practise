#String to Integer - Write your own atoi()

def atoi(s):
    i = 0
    n = len(s)

    # skip spaces
    while i < n and s[i] == ' ':
        i += 1

    sign = 1
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        i += 1

    num = 0
    MAX = (2**31) - 1
    MIN = -(2**31)

    while i < n and s[i].isdigit():
        digit = int(s[i])

        # ✅ fixed overflow check
        if num > MAX // 10 or (num == MAX // 10 and digit > (7 if sign == 1 else 8)):
            return MAX if sign == 1 else MIN

        num = num * 10 + digit
        i += 1

    return sign * num


while True:
    s = input("enter a string (exit to stop): ")
    if s == "exit":
        break
    print(atoi(s))
