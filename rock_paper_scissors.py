print("Rock Paper Scissors!")
input1 = input("Enter player 1's pick: ")
input2 = input("Enter player 2's pick: ")

if input1 == "Rock" and input2 == "Scissors":
    print("Player 1 wins!")
elif input1 == "Scissors" and input2 == "Rock":
    print("Player 2 wins!")

if input1 == "Rock" and input2 == "Paper":
    print("Player 2 wins!")
elif input1 == "Paper" and input2 == "Rock":
    print("Player 1 wins!")

if input1 == "Paper" and input2 == "Scissors":
    print("Player 2 wins!")
elif input1 == "Scissors" and input2 == "Paper":
    print("Player 1 wins!")

if input1 == input2:
    print("Tie Game.")
