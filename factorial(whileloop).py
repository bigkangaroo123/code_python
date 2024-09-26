#factorial formula: 4 = 3 * 2 * 1   n = (n-1) * (n-2) .... till it reaches 1 which is n - (n-1)
num = int(input("Enter a positive integer: "))

factorial = 1
i = num
while i > 0:
    factorial *= i #this is just a short form of factorial = factorial * i
    i -= 1
print(num, "factorial is ",factorial)
