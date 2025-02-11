#all prime numbers from 2 to n:
def find_primes(n):
    nums = []
    def helper(num):
        if num < 2:
            return False
        for i in range(2, int((num**0.5)+1)):
            if num % i == 0:
                return False
            
        return True
            
    for i in range(n):
        if helper(i):
            nums.append(i)

    return nums

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum








