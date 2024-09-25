print("Enter the last 4 digits of the phone number: ")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
    print("It's a telemarketer!!!!!!!!! STOOPPP DONT ANSWER")
else:
    print("Safe :D, u can answer :D")
