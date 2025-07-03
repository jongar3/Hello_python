import random

print("Welcome to rock paper and scissors")
play=True
while play==True:
    print("\tselect an option: ")
    player_index= int(input("0 rock \n1 paper\n2 scissors\n"))

    option= ["rock", "paper", "scissors"]
    
    if (player_index>2 or player_index<0):
        print("you introduce a non valid number")
        continue
    player= option[player_index]

    print(f"you choosed {player}")

    computer= random.choice(option)

    print(f"computer chossed {computer}")
    if (computer==player):
        print("You draw.")
    elif ((player == "paper") and (computer == "rock")) or ((player == "rock") and (computer == "scissors")) or ((player == "scissors") and (computer == "paper")):
        print("You win!")
    else:
        print("You lose.")
    play = int(input("Continue playing? (y=1, n=0)"))
