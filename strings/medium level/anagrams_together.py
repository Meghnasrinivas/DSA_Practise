# Print Anagrams TOgether

def grp_Anagrams(arr):
    groups={}
    for word in arr:
        key=' '.join(sorted(word))
        if key not in groups:
            groups[key]=[]
        
        groups[key].append(word)
    return list(groups.values())
        
while True:
    user_input = input("Give words separated by space (or type 'exit' to stop): ")
    
    if user_input.lower() == "exit":
        break
    
    arr = user_input.split()
    print(grp_Anagrams(arr))