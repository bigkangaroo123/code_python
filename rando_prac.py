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

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i+1) #creating a list of 1s 
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))  # Get width for alignment
    for row in triangle:
        row_string = " ".join(map(str, row))  # Convert list to string
        print(row_string.center(max_width))  # Center align

# Example usage:
n = 6  # Number of rows
triangle = pascal_triangle(n)
print_triangle(triangle)






