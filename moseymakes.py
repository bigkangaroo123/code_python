# more than c consonants OR v vowels, not a word

def c_checker(c, word):
    cons = "bcdfghjklmnpqrstvwxyz"
    counter = 0
    for char in word:
        if char in cons:
            counter += 1
        else:
            counter = 0
        
        if counter > c:
            return False
        
    return True

def v_checker(v, word):
    vowels = "aeiouy"
    counter = 0
    for char in word:
        if char in vowels:
            counter += 1
        else:
            counter = 0

        if counter > v:
            return False
        
    return True

n, c, v = map(int, input().split())
word = input()

if c_checker(c, word) and v_checker(v, word):
    print("YES")
else:
    print("NO")