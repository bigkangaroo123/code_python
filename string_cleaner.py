def cleaner(word): #kinda like methods in java
    result = ""
    for char in word:
        if char.isalpha(): #isaplha checks if all chars are alphabets
            result += char.lower()
    return result

word = cleaner(input("Enter a string: "))

print(f"word is: {word}")
    
