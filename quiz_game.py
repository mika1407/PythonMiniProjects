print("Welcome to my computer quiz!!")

playinig = input("Do you want to play? ")

if playinig.lower() != "yes":
    quit()

print("Ok! lets play :)")
score = 0  

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Finland? ")
if answer.lower() == "helsinki":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What year was Tampere founded? ")
if answer.lower() == "1779":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 4 points")
print("You got " + str((score/4)*100) + "%.")