def fib(num):
    memory = {0 : 0,1 : 1}

    def helper(x):
        if x in memory: #if x is 0 or 1
            return x #as if it's 1 then its fib is 1, if its 0, its fib is 0
        else:
            return helper(x-1) + helper(x-2)
            #this eventually comes down to 1 which is in the memory which will exit the program

    return helper(num)

print(f"{fib(10)}")

#WAY FUCKING EASIER WITHOUT A DICTIONARY:
'''
def fib(i): #takes in an index
    if i == 0 or i == 1:
        return i
    else:
        return fib(i-2) + fib(i-1)

num = int(input("Enter a positive integer: "))
print(f"{fib(num)}")
'''
