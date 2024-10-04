def compare(word1, word2):
    shared = []
    for char in word1:
        if char in word2:
            shared.append(char)
    return shared

a = input("Enter a word: ")
b = input("Enter another word: ")
shared = compare(a, b)
if len(shared) == 0:
    print("no common chararcters")
else: 
    print(shared)
