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
elif x > 0 and y == 0:
    print("On the X axis, between Q1 and Q4")
elif x < 0 and y == 0:
    print("On the X axis, between Q2 and Q3")
elif x == 0 and y > 0:
    print("On the Y axis, between Q1 and Q2")
elif x == 0 and y < 0:
    print("On the Y axis, between Q3 and Q4")
else:
    print("Origin")
