# First non-repeating character of given string

s1='geeksforgeeks'
dict1={}
for i in range(len(s1)):
    if s1[i] in dict1:
        dict1[s1[i]]+=1
    else:
        dict1[s1[i]] = 1
print(dict1)
for char in dict1:
    if dict1[char] ==1:
        print(char)
        break
   