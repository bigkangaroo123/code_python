def output(num):
    text = ''
    for i in range(1, num + 1): 
        if i % 2 == 0:
            #if i is even
            text += '0'
        else:
            text += '1' #first number will always be 1 since 1 is the first value to enter this function

    return text

def pattern(num):
    for i in range(1, num+1):
        print(output(i)) #runs the output function for every value from 1 to num 

    #its not mandatory to have return statements

a = int(input("Enter an integer that is >1: "))
b = pattern(5)
print(b)
