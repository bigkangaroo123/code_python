def palindrome_checker(word) -> bool: #its like hinting what the function returns - doesnt mean anything tho
    word = word.lower()
    return word == word[::-1] #return true or false

a = input("Enter a word: ")
is_palindrome = palindrome_checker(a)
if is_palindrome:
    print(f"the word {a} is indeed a palindrome")
else:
    print(f"the word {a} is indeed not a palindrome")
