import math

def finding_pair(average):
    #the 2 prime nums
    for a in range(2, average):
        if is_prime(a):
            b = 2*average - a
            if is_prime(b):
                return f"{a} {b}"

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

t = int(input())
means = []
for i in range(t):
    user_input = int(input())
    means.append(user_input)

for i in range(0, len(means)):
    print(finding_pair(means[i]))

