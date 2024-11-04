#machine #1: 30 quarters every 35th time played
#machine #2: 60 quarters every 100th time played
#machine #3: 9 quarters every 10th time played

#each play costs 1 quarter

#input: number of quarters (1 to 1000)
#input 2: number of times each machine has been played (3 inputs after that)
#output: number of times she can play until broke

def reset(num):
    return 0

quarters = int(input("how manu quarters? (1 to 1000): "))
print("how many times has each machine been played?: ")
m1 = int(input())
m2 = int(input())
m3 = int(input())

counter = 0

while quarters > 0:
    quarters -= 1 #1 quarter down each play
    counter += 1
    m1 += 1 #machine 1 has been played once
    if m1 == 35: #if 35 plays
        quarters += 30
        m1 = reset(m1)
    if quarters == 0:
        break

    quarters -= 1 #1 quarter down each play
    counter += 1
    m2 += 1 #machine 2 has been played once
    if m2 == 100: #if 35 plays
        quarters += 60
        m2 = reset(m2)
    if quarters == 0:
        break

    quarters -= 1 #1 quarter down each play
    counter += 1
    m3 += 1 #machine 1 has been played once
    if m3 == 10: #if 35 plays
        quarters += 9
        m3 = reset(m3)
    if quarters == 0:
        break

print(counter)
