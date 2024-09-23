first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
name = first_name + " " + last_name
print("Welcome, ",name,"!")

birth_year = int(input("Please enter your birth year: "))
current_year = int(input("Please enter current year: "))

age = current_year - birth_year
over18 = False
if age < 0:
    print("Invalid input")
else:
    if age >= 18:
        over18 = True

print("You are (age) years old")
if over18 == True:
    print("You are old enough to drink!")
else:
    print("You are not old enough to drink")
