def mergesort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = mergesort(array[:mid])  # Left half
    right = mergesort(array[mid:])  # Right half

    return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # Append remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

def is_prime1(num, i=None): #i is the divisor
    if 0 < num <= 2:
        return True

    if i is None:
        i = num - 1 #initialize the divisor

    if i == 1:
        return True #when divisor reaches 1, num is prime
    
    if num % i == 0:
        return False

    return is_prime1(num, i-1)

def is_prime(num):
    def helper(num, divider):
        if num == divider:
            return True
        else:
            if num % divider == 0:
                return False
            else:
                return helper(num, divider+2)
    
    if num == 1:
        return False
    elif num in {2,3}:
        return True
    elif num % 2 == 0:
        return False
    else:
        return helper(num, 3)

def sum_of_binary(binary):
    if not binary:
        return 0
    if binary == '0':
        return 0
    if binary == '1':
        return 1
    return int(binary[0]) + sum_of_binary(binary[1:])
    
num = input()
print(sum_of_binary(num))
