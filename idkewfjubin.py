a, b = map(int, input().split())


for i in range(a):
    word = input()
    og = 0
    works = True
    if word.count(word[0]) == 1:
        og = 0
    else:
        og = 1
    for i in range(len(word)-1):
        if word.count(word[i+1]) == 1 and og == 0:
            works = False
            break
        elif word.count(word[i+1])>1 and og == 1:
            works = False
            break
        else:
            if og == 0:
                og = 1
            elif og == 1:
                og = 0
    if works == True:
        print("T")
    else:
        print("F")