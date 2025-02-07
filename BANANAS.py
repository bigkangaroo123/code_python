ongoing = True
words = []
while ongoing:
    inp = input()
    if inp == "X":
        break
    else:
        words.append(inp)
        
def is_monkey(word): --> bool
    if "A" not in word or "N" not in word or "S" not in word or "B" not in word:
        return False
    elif len(word) == 1 and (word != "S" or word != "B"):
        return True
    else:
        for i in range(len(word))
        
    
#end is is_monkey()
        
outputs = []
for i in range(len(words)):
    is words[i]
