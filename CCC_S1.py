#1st yr: pink ticket
#2nd yr: green
#3rd: red
#4th: orange

#unique price
#minimize printig cost

#cost of each ticket:
pink = int(input()) 
green = int(input())
red = int(input())
orange = int(input())

money = int(input())

tickets = [pink, green, red, orange]
colours = ["pink", "green", "red", "orange"]

all_combinations = []
min_cost = None

sum = 0
for p in range(target // pink + 1):
    for g in range(target // green + 1)):
        for r in range(target // red + 1):
            for o in range(target // orange + 1):
                if p*pink + g*green + r*red + o*orange == money:
                    all_combinations.append((p, g, r, o))
                    if P+g+r+o < min_
                
    
