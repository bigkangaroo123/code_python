data = [7, 21, 5, 19, 6, 2]
k = len(data) - 1
a = 1
b = 0
while k >= 0:
    if data[k] % 2 < 1: #checks if data[k] is even
        a = a * data[k] #a = every even value in data, multiplied
    else:
        b += 1 #b = number of odd numbers in data
    k -= 1

print(a)
print(b)
