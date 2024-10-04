def composite_or_prime(arg):
    factors = []
    factors2 = []
    for i in range(2, arg):
        if arg % i == 0:
            factors2.append(i)
    if len(factors2) == 0:
        return True
    
    for i in range(1, arg+1):
        if arg % i == 0:
            factors.append(i)
    return factors
    
num = int(input("Enter an integer: "))
factors = composite_or_prime(num)
print(factors)
