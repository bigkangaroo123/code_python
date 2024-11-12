def p(word, tail = True):
    if not word or len(word) == 1:
        return True
    
    if word[0] != word[-1]: #immediate false is 1st and last value dont match
        return False
    
    if not tail:
        return False
    
    else:
        return p(word[1:-1], word[0] == word[-1])

u_input = input()
print(p(u_input))
        
