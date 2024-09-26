num = int(input("Enter positive integer: "))
print("The factor(s) are: ")
for i in range(1, num+1):
    if num % i == 0:
        print(i)
