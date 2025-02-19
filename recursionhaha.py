def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def sumn(n):
    if n == 1:
        return 1
    return n + sumn(n-1)

def rstring(s):
    if len(s) == 1:
        return s
    return s[-1] + rstring(s[:-1])

def countzeros(n, zeros=0):
    if n == 0:
        return 1
    return zeros+countzeros(n//10)
print(countzeros(1000))
