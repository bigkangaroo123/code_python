import random

choices = ["Rock", "Paper", "Scissors"]
choice = random.choice(choices)

choices2 = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]
print("Rock, paper, scissors!")
user_choice = input("Enter your choice: ")
if user_choice not in choices2:
    print("Invalid input")
else:
    print("Computer's choice:", choice)
    if (choice == "Rock" or choice == "rock") and (user_choice == "Paper" or user_choice == "paper"):
        print("YOU WONNNNNNNNN LFGGG")
    elif (choice == "Rock" or choice == "rock") and (user_choice == "Scissors" or user_choice == "scissors"):
        print("Computer won :(")
    elif (choice == "Paper" or choice == "paper") and (user_choice == "Scissors" or user_choice == "scissors"):
        print("YOU WONNNNNNNNN LFGGG")
    elif (choice == "Paper" or choice == "paper") and (user_choice == "Rock" or user_choice == "rock"):
        print("Computer won :(")
    elif (choice == "Scissors" or choice == "scissors") and (user_choice == "Paper" or user_choice == "paper"):
        print("Computer won :(")
    elif (choice == "Scissors" or choice == "scissors") and (user_choice == "Rock" or user_choice == "rock"):
        print("YOU WONNNNNNNNN LFGGG")
    else:
        print("It's a tie :/")
