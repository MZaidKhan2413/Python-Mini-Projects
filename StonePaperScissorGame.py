# Program to play Stone Paper Scissor :
import random as R

print("\n****|WELCOME TO STONE PAPER SCISSOR GAME|****\n")

while True :

    player = int(input("1 = Stone\n2 = Paper\n3 = Scissor\nEnter your choice : "))
    if player >=1 and player<=3:
        pass
    else :
        print("Inavlid Input !")
        break

    roboChoice = ["Stone","Paper","Scissor"]
    computer = R.choice(roboChoice)
    print(f'\nComputer chose : {computer}\n')
    if computer=="Stone":
        robo = 0
    elif computer=="Paper":
        robo = 1
    else :
        robo = 2

    game = [
        ["Draw","Lose","Won"],
        ["Won","Draw","Lose"],
        ["Lose","Won","Draw"]
    ]

    print("     ",game[player-1][robo],"\n")

    ask = input("Do want to play again? ")
    if ask.lower()=="no" or ask.lower()=="n":
        print("\n")
        break