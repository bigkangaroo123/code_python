def string_to_list(string):
    '''to convert a string with numbers seperated by commas to a list

    argument
        string: string of the numbers

    return
        list of the string numbers converted to integers
    '''
    a = string.split(",") #.split() splits the string input, can choose seperated, in this case its a comma
    a_list = []
    for num in a:
        a_list.append(int(num))
    return a_list

b = input("Enter numbers: ")
ints = string_to_list(b)
print(ints)

from random import randrange
def random_ints(start, end, frequency):
    if start < end and frequency > 0:
        rand_list = []
        while frequency > 0:
            num = randrange(start, end + 1)
            rand_list.append(num)
            frequency -= 1
        return rand_list
    else:
        return []
s = int(input("Enter a starting value: "))
e = int(input("Enter last value: "))
f = int(input("How many random integers?: "))
rand_ints = random_ints(s, e, f)
print(rand_ints)
