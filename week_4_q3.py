def odd_and_even(array):
    k = len(data) - 1
    a = 1
    b = 0
    while k >= 0:
        if data[k] % 2 == 0: #checks if data[k] is even
            a = a * data[k] #a = every even value in data, multiplied
        else:
            b += 1 #b = number of odd numbers in data
        k -= 1
    temp = [a, b]
    return temp
        
print("Enter 10 integer values: ")
data = []
for i in range(10):
    num = int(input())
    data.append(num)

final = odd_and_even(data)
print(final[0])
print(final[1])
