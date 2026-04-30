# Roman to Integer Conversion

def reomen(s1):
    romen={'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    }
    total=0
    for i in range(len(s1)-1):
        if romen[s1[i]] < romen[s1[i+1]]:
             total-=romen[s1[i]]
        else:
            total+=romen[s1[i]]
    total+=romen[s1[-1]]
    return total

s1=input('enter roman number (valid): ')
print(reomen(s1))