N = 1216
x = 0
while N > 0:
    x = x + N % 10
    N = N/10
    #end
print(x)

#program adds all the remainders of N divided by 10, reducing the value by N/ 10 each time
