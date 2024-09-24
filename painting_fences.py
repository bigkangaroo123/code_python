import math

section1 = input("How many fences in section 1?: ")
section2 = input("How many fences in section 2?: ")
section3 = input("How many fences in section 3?: ")

cans = int(len(section1) + len(section2) + len(section3))
final_cans = cans - (cans % 12)
leftover = cans - final_cans
cost = (final_cans // 12) * 14.95

print(f"You'd need {final_cans} cans")
print(f"You'd have {leftover} leftover cans")
print(f"It would cost you ${cost}")
