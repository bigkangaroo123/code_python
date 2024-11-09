time = int(input()) #the minutes
chores = int(input()) #the number of chores
chores_time = [] 
for i in range(chores): #time it takes to complete each chore
    t = int(input())
    chores_time.append(t)

chores_time = sorted(chores_time) #sorted bc most amt of chores in least amt of time
sum_time = 0
counter = 0

for i in chores_time:
    if sum_time + i > time:
        break
    sum_time += i
    counter += 1

print(counter)