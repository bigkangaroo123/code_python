n = int(input())
l = input().split()
o = input().split()
b = False
s = 0
for i in range(n):
    if l[i] == o[i]:
        if not b:
            b=True
            s+=1
    else:
        if b:
            b=False
print(s)