n = int(input())
m = int(input())
if m-n == 0 or m-n == 1:
    print("stressed")
elif m-n < 0:
    print("relaxed")
else:
    print("okay")