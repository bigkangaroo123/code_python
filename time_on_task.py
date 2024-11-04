#input #1: how many minutes u have? (from 0 to 100,000)
#input #2: how many chores? (from 0 to 100)
    #input(s): how many minutes for each chore

t = int(input("how many minutes u have?: "))
c = int(input("how many chores u have to do?: "))
m = []
print("how many minutes for each chore?: ")
for i in range(c):
    temp = int(input())
    m.append(temp)

m.sort() #from least to greatest which gives the most amt of chores done
time_spent = 0
result = 0
for time in m:
    if time + time_spent <= t:
        time_spent += time
        result += 1
    else:  
        break
    
print(result)
        
        
            
