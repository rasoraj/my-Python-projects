import random

c_score = 0
u_score = 0

print("Your game starts now")

while c_score < 3 and u_score < 3:

    user = input("Give your shot : ")

    comp = random.choice(['rock', 'paper', 'scissor', 'rock', 'paper', 'scissor'])
    print("comp : " + comp)

    if user == "rock" and comp == "paper":
        c_score = c_score + 1
        print("comp won!")
    if user == "rock" and comp == "scissor":
        u_score = u_score + 1
        print("you won!")
    if user == "paper" and comp == "rock":
        u_score = u_score + 1
        print("you won!")
    if user == "paper" and comp == "scissor":
        c_score = c_score + 1
        print("comp won!")
    if user == "scissor" and comp == "rock":
        c_score = c_score + 1
        print("comp won!")
    if user == "scissor" and comp == "paper":
        u_score = u_score + 1
        print("you won!")
    if user == comp:
        print("Game Draw")

    print("Next Game :=========")

if u_score == 3:
    print("You've won the Game, Congratulations!")
else:
    print("Ooops!! Next time luck will favour you :)")