l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [l1[i] for i in range(len(l1)-1, -1, -1)]
#w list comprehension :D

doubles = [2*i for i in range(1, 11) if 2*i%10 != 0]
triples = [3*i for i in range(1, 11)]
squares = [z**2 for z in range(1, 11)]
# print(doubles)
# print(triples)
# print(squares)

fruits = ['mango', 'orange', 'banana', 'coconut']
fruits = [i[0].upper() + i[1].upper() + i[2:] for i in fruits]
# print(fruits)

numbers = [-10, 25, 0, -7, 42, 8, -3, 19]
posnums = [-i if i < 0 else i for i in numbers]
# print(posnums)

grades = [95, 78, 84, 62, 47, 100, 89, 73, 56, 91]
passing = [i for i in grades if i >= 75]
# print(passing)

options = ["any", "albany", "apple", "world", "helo", ""]
filtered = [i for i in options if len(i) >= 2 and i[0] ==  "a" and i[-1] == "y"]
# print(filtered)

#flattening a mattrix: making a list of lists (like the sudoku board)
matrix = [[1, 4, 5], [2, 3, 5], [7, 8, 9]]
flattened = [i for row in matrix for i in row]
# print(flattened)

nums = [12, 5, 18, 0, 32, 7, 11, 22, 9, 6, 28, 19, 14, 0, 17]
catagories1 = ["Even" if i%2==0 else "Odd" for i in nums]
catagories = {i: "Even" if i%2==0 else "Odd" for i in nums}
print(catagories1)
print(catagories)

matrix3d = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
# print(matrix3d)

def is_even(n):
    return "Even" if n%2==0 else "Odd"

#using the same nums list
filter2 = [is_even(i) for i in nums]
print(filter2)