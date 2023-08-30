print("Welcome to my computer quiz!!")

playinig = input("Do you want to play? ")

if playinig.lower() != "yes":
    quit()

print("Ok! lets play :)")  

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')