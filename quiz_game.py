
point = 0

print("Let's play the quiz game!")

playing = input("Do you want to play the game? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer == "read only memory":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "graphic processing unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

print(f"You have answered {point} questions right. That is", point/4*100, "%.")


