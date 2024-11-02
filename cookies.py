money = float(input("How much money do you have right now?: $"))
n_cookies = int (input("How many normal cookies sold?: "))
b_cookies = int(input("How many big cookies sold?: "))

total_cookies = n_cookies + b_cookies
cost_cookies = n_cookies * 0.50 + b_cookies * 0.75
cost_sales = n_cookies * 1.25 + b_cookies * 2.00
profit = cost_sales - cost_cookies
money = money + profit

print(f"In total, {total_cookies} were sold")
print(f"You made a profit of ${profit}")
print(f"The money you have after selling all the cookies is ${money}")
