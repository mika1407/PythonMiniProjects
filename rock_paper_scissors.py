import random
from stringcolor import *

user_wins = 0
computer_wins = 0
tie = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 2, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print(cs("User won!", "blue"))
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print(cs("User won!","blue"))
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print(cs("User won!", "blue"))
        user_wins += 1

    elif user_input == computer_pick:
        print(cs("Its a tie", "yellow"))
        tie += 1

    else: 
        print(cs("Computer win!", "green"))
        computer_wins += 1

print(cs("Results:","yellow"))
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Number of ties: ", tie)
print(cs("Goodbye!", "red"))