def palindrome_checker(word) -> bool: #its like hinting what the function returns - doesnt mean anything tho
    if not word:
        return True
    elif len(word) == 1:
        return True
    else:   
        word = word.lower()
        return word == word[::-1] # :: sorts a string based on the argument, ex - -2 would've been switching every 2 indexes of the word
        #return true or false

a = input("Enter a word: ")
is_palindrome = palindrome_checker(a)
if is_palindrome:
    print(f"the word {a} is indeed a palindrome")
else:
    print(f"the word {a} is indeed not a palindrome")
