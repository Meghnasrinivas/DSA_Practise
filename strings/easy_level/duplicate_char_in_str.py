#Print all the duplicate characters in a string

str1='geekforgeeks'
count={}
for char in range(len(str1)):
    if str1[char] in count:
        count[str1[char]] +=1
    else:
        count[str1[char]] = 1
print(count)
for i in count:
    if count[i] >1:
        print(i,'count',count[i])