# 2 units per second
# z axis: 
#   - if zi < z: climb vertically with z seconds
#   - if zi > z: they glide the whole way
#       - meaning 3 u/s forward, 4 u/s downward
import math

x, y, z = map(int, input().split())
n = int(input())
hs = []
for i in range(n):
    xi, yi, zi = map(int, input().split())
    hs.append((xi, yi, zi))

times = []
for tup in hs:
    if (x, y, z) == tup:
        break

    elif tup[2] == z:
        xtime = (abs(tup[0]) - x) / 2
        ytime = (abs(tup[1]) - y) / 2
        times.append(xtime+ytime)

    elif tup[2] < z:
        ztime = z - tup[2]
        xtime = (abs(tup[0]) - x) / 2
        ytime = (abs(tup[1]) - y) / 2
        times.append(ztime+xtime+ytime)
        

print(min(times))