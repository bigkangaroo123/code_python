n = int(input())
l = input().split()
o = input().split()
b = False
s = 0
for i in range(n):
    if l[i] == o[i]:
        if b:
            continue
        else:
            b=True
            s+=1
    else:
        b = False
        
print(s)