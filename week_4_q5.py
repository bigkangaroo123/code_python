def isAbundant(data):
    abundant_even = []
    abundant_odd = []
    for i in data:
        if i % 2 == 0:
            factors = []
            for j in range(1, i):
                if i % j == 0:
                    factors.append(j)
                if sum(factors) > i:
                    abundant_even.append(i)
                    factors.clear()
        else:
            factors = []
            for j in range(1, i):
                if i % j == 0:
                    factors.append(j)
                if sum(factors) > i:
                    abundant_odd.append(i)
                    factors.clear()
    return f" {abundant_even} are even abundant and {abundant_odd} are odd abundant"

'''
def abundant_or_deficient_or_perfect(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    #end
    sum_of_factors = sum(factors)
    if sum_of_factors < num:
        return "deficient"
    elif sum_of_factors == num:
        return "PERFECT NUMBE!!11!1"
    else:
        return "abundant"
#end
num = int(input("Enter a positive integer: "))
choice = abundant_or_deficient_or_perfect(num)
print(choice)
'''

print("Enter 10 positive integers: ")
data = []
for i in range(10):
    data.append(int(input()))
    #end
print(isAbundant(data))
