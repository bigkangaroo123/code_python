
def is_monkey(word) -> bool:
    if word == "A" or word == "":
        return True
    
    if word.startswith("A") and "N" in word:
        n_index = word.index("N")
        return is_monkey(word[1:n_index]) and is_monkey(word[n_index+1:])
    
    if word.startswith("B") and word.endswith("S"):
        return is_monkey(word[1:-1])

    if "N" in word:
        n_index = word.index("N")
        return is_monkey(word[:n_index]) and is_monkey(word[n_index+1:])

    return False

words = []
while True:
    inp = input().strip()
    if inp == "X":
        break
    else:
        words.append(inp)
        
for word in words:
    if is_monkey(word):
        print('YES')
    else:
        print('NO')

