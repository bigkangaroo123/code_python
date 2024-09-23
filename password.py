import random

length = int(input("How many characters should be in the password: "))

lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
specials = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 126))

pwd_temp = lowercase.copy()

upper = input("Include uppercase charactesrs? (y/n): ")
if upper == "Y" or upper == "y":
    pwd_temp.extend(uppercase)

numbers = input("Include digits? (y/n): ")
if numbers == "Y" or numbers == "y":
    pwd_temp.extend(digits)

special = input("Include special charactesrs? (y/n): ")
if special == "Y" or special == "y":
    pwd_temp.extend(specials)

pwd_final = ""

while len(pwd_final) != length:
    temp = chr(random.choice(pwd_temp)) #chr() translates the numbers from ASCII system to actual characters
    pwd_final = pwd_final + temp

print("Generated password: ",pwd_final)
    
