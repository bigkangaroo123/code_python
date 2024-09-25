x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

if x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
elif x > 0 and y < 0:
    print("Quadrant 4")
