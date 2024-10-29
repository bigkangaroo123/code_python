from math import sqrt

def factors(n, k):
    factors = [1, n]
    sqrtn = int(sqrt(n) + 1)
    for i in range(2, sqrtn):
        if n % i == 0:
            factors.append(i)
            j = n // i
            if j != i:
                factors.append(j)
    factors.sort()
    if len(factors) <= k:
        return "no"
    else:
        return factors[k-1]

print(factors(12, 3))


#idk = [3, 1, 4, 1, 5, 9]
#split list until len of list == 1
#its very easy to combine a sorted list in a bigger sorted list
#we just compare the 2 values to sort them
#now merge :)
#[3] [1] [4] [1] [5] [9]
# [1, 3] [4] [1, 5] [9]
#  [1, 3, 4] [1, 5, 9]
#   [1, 1, 3, 4, 5, 9]
#THIS IS CALLED MERGE SORT
#then delete any duplicates (convert to set and then to list again)
