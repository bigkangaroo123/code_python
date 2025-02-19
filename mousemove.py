c, r = map(int, input().split())

allx = []
ally = []

while True:
    x, y = map(int, input().split())
    if (x, y) == (0, 0):
        break
    else:
        allx.append(x)
        ally.append(y)

sumx = 0
sumy = 0
n = len(allx)
for i in range(n):
    if allx[i]+sumx<0:
        sumx = 0
    elif sumx+allx[i] >= c:
        sumx = c
    elif allx[i] > c:
        sumx += 0
    else:
        sumx += allx[i]

    if ally[i]+sumy<0:
        sumy = 0
    elif sumy+ally[i]>r:
        sumy = r
    elif ally[i] > r: 
        sumy += 0
    else:
        sumy += ally[i]

    print(sumx," ",sumy)