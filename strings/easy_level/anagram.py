# Check if two Strings are Anagrams of each other

def are_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    sorted_s1=sorted(s1)
    sorted_s2=sorted(s2)
    
    if sorted_s1==sorted_s2:
        print(f'{s1},{s2} are anagram')
    else:
        print(f'{s1},{s2} are not anagram')
    
s1=input('enter str : ')
s2=input('enter str again : ')
are_anagram(s1,s2)