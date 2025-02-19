e = input().upper()
n = int(input())
moves = [] 
for i in range(n):
    x, type2 = input().split()
    x = int(x)
    moves.append((type2, x))

max_dmg = 0
if e == "FIRE":
    for tup in moves:
        if tup[0] == "GRASS":
            if tup[1]//2 > max_dmg:
                max_dmg = tup[1]//2
        elif tup[0] == "FIRE":
            if tup[1] > max_dmg:
                max_dmg = tup[1]
        else:
            if tup[1]*2 > max_dmg:
                max_dmg = tup[1]*2

elif e == "WATER":
    for tup in moves:
        if tup[0] == "GRASS":
            if tup[1]*2 > max_dmg:
                max_dmg = tup[1]*2
        elif tup[0] == "FIRE":
            if tup[1]//2 > max_dmg:
                max_dmg = tup[1]//2
        else:
            if tup[1] > max_dmg:
                max_dmg = tup[1]

elif e == "GRASS":
    for tup in moves:
        if tup[0] == "GRASS":
            if tup[1] > max_dmg:
                max_dmg = tup[1]
        elif tup[0] == "FIRE":
            if tup[1]*2 > max_dmg:
                max_dmg = tup[1]*2
        else:
            if tup[1]//2 > max_dmg:
                max_dmg = tup[1]//2

print(max_dmg)