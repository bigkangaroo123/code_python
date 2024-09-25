print("Enter time:")
hour = int(input("What hour is it?: "))
minute = int(input("What minute is it?: "))\

#open at 9 00, closes at 18 30
if hour < 9 or (hour > 18 and minute > 30) or hour > 18:
    print("Closed")
else:
    print("Open")
