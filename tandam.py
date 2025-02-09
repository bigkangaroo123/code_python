def type1(n, dmoj, peg):
    dmoj = sorted(dmoj)
    peg = sorted(peg)

    min_speed = 0
    for i in range(n):
        temp = max(dmoj[i], peg[i])
        min_speed += temp
    
    return min_speed

def type2(n, dmoj, peg):
    dmoj = sorted(dmoj)
    peg = sorted(peg, reverse=True)

    max_speed = 0
    for i in range(n):
        temp = max(dmoj[i], peg[i])
        max_speed += temp
    
    return max_speed

choice = int(input())
n = int(input())
dmoj = list(map(int, input().split()))
peg = list(map(int, input().split()))

if choice == 1:
    min_speed = type1(n, dmoj, peg)
    print(min_speed)
else:
    max_speed = type2(n, dmoj, peg)
    print(max_speed)
