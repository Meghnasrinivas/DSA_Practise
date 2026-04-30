# Check if Strings Are Rotations of Each Other

s1=input('enter first string : ')
s2=input('enter second string : ')
x=''
if len(s1)!=len(s2):
    print(0)
    exit()
x=s1+s1
if x.count(s2)>0:
    print('ROTATION IS TRUE')
else:
   print('ROTATION IS FALSE')