n, c, v = map(int, input().split())
word = input()

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"

c_checker = 0
v_checker = 0

nice = True

for char in word:
    if char in consonants:
        c_checker += 1
        v_checker = 0
    elif char in vowels:
        v_checker += 1
        c_checker = 0
    elif char == 'y':
        c_checker += 1
        v_checker += 1


    if c_checker > c or v_checker > v:
        nice = False
        print("NO")
        break

if nice:
    print("YES")