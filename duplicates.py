def compare(word1, word2):
    shared = set() #round braces is a set, use set to avoid duplicates
    #also, initate a set like set(), not like a list just []
    for char in word1:
        if char in word2:
            shared.add(char)
    return shared

a = input("Enter a word: ")
b = input("Enter another word: ")
shared = compare(a, b)
if len(shared) == 0:
    print("no common chararcters")
else: 
    print(shared)
