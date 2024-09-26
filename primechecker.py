num = int(input("Enter an integer that is >1: "))
factors = []
for i in range (2, num):
    if num % i == 0:
        factors.append(i)

if len(factors) == 0:
    print("It's a prime number")
else:
    print("It's a composite number")
