time = int(input())
chores = int(input())
chores_time = []
for i in range(chores):
    t = int(input())
    chores_time.append(t)

chores_time = sorted(chores_time)
sum_time = 0
counter = 0
for i in chores_time:
    if sum_time + i > time:
        break
    sum_time += i
    counter += 1
    

print(counter)