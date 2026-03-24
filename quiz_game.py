print("welcome to the quiz game! ")
playing = input("do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay! let's play :) ")
score = 0
answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct! ")
    score += 1
else:    print("incorrect! ")
answer = input("what does ram stand for? ")
if answer.lower() == "random access memory":
    print("correct! ")
    score += 1
else:    print("incorrect! ")
answer = input("what does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct! ")
    score += 1
else:    print("incorrect! ")
answer = input("The clock rate of CPU is measured in which unit? ")
if answer.lower() == "ghz":
    print("correct! ")
    score += 1
else:    print("incorrect! ")
answer = input("what does ssd stand for? ")
if answer.lower() == "solid state drive":
    print("correct! ")
    score += 1
else:    print("incorrect! ")
print("you got " + str(score) + " questions correct! ")
print("you got " + str((score / 5) * 100) + "%")
      
