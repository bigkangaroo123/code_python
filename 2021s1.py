n = int(input())
ways = 0

for i in range(n//4+1):
    if (n - 4*i) % 5 == 0:
        ways += 1

print(ways)