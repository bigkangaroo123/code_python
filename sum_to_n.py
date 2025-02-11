# def sum1(n, val=0):
#     #O(n)
#     for i in range(1, n+1):
#         val += i
#     return val

# def sum2(n):
#     #O(1)
#     return (n*(n+1)) // 2

# n = int(input())
# print(sum2(n))
# print(sum1(n))

n = int(input())
while n:
    t = int(input())
    n -= 1

    #holy shit this actyually works