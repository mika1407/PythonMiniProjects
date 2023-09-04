from stringcolor import *

name = input(cs("type your name: ", "red"))
print("Welcome", name, "to this adventure!")

answer = input(cs("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ", "yellow")).lower()

if answer == "left":
    answer = input(cs("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ","orange"))

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(cs("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ","blue"))

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print(cs("You talk to the stanger and they give you gold. You WIN!", "red"))
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)