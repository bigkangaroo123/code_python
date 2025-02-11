def solve(word):
    letter_counter = {}
    for char in word:
        if char in letter_counter:
            letter_counter[char] += 1
        else:
            letter_counter[char] = 1

    pattern = []
    for char in word:
        if letter_counter[char] > 1:
            pattern.append(True)
        else:
            pattern.append(False)
    
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[i-1]:
            return "F"
    
    return "T"


t, n = map(int, input().split())
outputlist = []

while t:
    word = input()
    outputlist.append(solve(word))
    t-=1

for _ in outputlist:
    print(_)