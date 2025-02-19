#seat number = hat number
n = int(input())
ppl = []
t = n
while t:
    num = int(input())
    ppl.append(num)
    t-=1

mid = n // 2
result = 0

for i in range(mid):
    if ppl[i] == ppl[mid+i]:
        result += 2
    
print(result)