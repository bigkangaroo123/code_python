def consonant_counter(word):
    result = 0
    chars = []
    for i in word:
        chars.append(i)
    for char in chars:
        if char == "a" or char == "e" or char ==  "i" or char == "o" or char == "u" or char == "A" or char == "E" or char ==  "I" or char == "O" or char == "U":
            chars.remove(char)
    result = len(chars)
    return result

a = input("Enter a word: ")
consonant = consonant_counter(a)
print(f"There are {consonant} consonants in {a}")
