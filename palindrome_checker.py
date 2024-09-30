def palindrome_checker(word):
    word = word.lower()
    return word == word[::-1]

a = input("Enter a word: ")
is_palindrome = palindrome_checker(a)
if is_palindrome:
    print(f"the word {a} is indeed a palindrome")
else:
    print(f"the word {a} is indeed not a palindrome")
