#Snakes and Ladders

solved = False

while not solved:
    position = 1
    while position < 100:
        u_input = int(input())
        if u_input == 0:
            print("You Quit")
            solved = True
            break
        
        elif u_input <= 12 and u_input >= 2:
            position += u_input

            if position == 100:
                print(f"You are now on square 100")
                print("You win!")
                solved = True
                break

            elif position > 100:
                position -= u_input

            #Ladders:
            if position == 9:
                position = 34
            elif position == 40:
                position = 64
            elif position == 67:
                position = 86

            #Snakes:
            if position == 54:
                position = 19
            elif position == 90:
                position = 48
            elif position == 99:
                position = 77

            print(f"You are now on square {position}")
            
        else:
            print("Please enter a number between 2 and 12, according to the values of a dice")
            

    