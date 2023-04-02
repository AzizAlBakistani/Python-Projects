import random
while(True):
    i = input(print("Do you want to play Rock Paper Scissors? Y/N : "))
    if i=="Y" or i=="y": #user input
        us = 0 #user score
        cs = 0  #computer Score
        for i in range(0,5):
            g = input(print("Your Turn :")) #user guess
            g= g.capitalize()
            r = random.randrange(0, 3)
            l = ["Rock", "Paper", "Scissors"]
            cp = l[r] #computer guess
            if g==cp:
                print("Computer :",l[r])
                print ("Draw")
                print("Your Score: " , us)
                print("Computer Scor: ", cs)
            elif g=="Rock" and cp=="Scissors":
                print("Computer :", l[r])
                print("You Win")
                us=us+1
                print("Your Score: " , us)
                print("Computer Score: " , cs)
            elif g=="Rock" and cp=="Paper":
                print("Computer :", l[r])
                print("Computer Wins")
                cs=cs+1
                print("Your Score: " , us)
                print("Computer Score: " , cs)
            elif g=="Paper" and cp=="Scissors":
                print("Computer :", l[r])
                print("Computer Wins")
                cs=cs+1
                print("Your Score: " , us)
                print("Computer Score: " , cs)
            elif g=="Paper" and cp=="Rock":
                print("Computer :", l[r])
                print("You Win")
                us = us+1
                print("Your Score: " , us)
                print("Computer Score: " , cs)
            elif g=="Scissors" and cp=="Rock":
                print("Computer :", l[r])
                print("Computer Wins")
                cs=cs+1
                print("Your Score: " , us)
                print("Computer Scor: " , cs)
            elif g=="Scissors" and cp=="Paper":
                print("Computer :", l[r])
                print("You Win")
                us=us+1
                print("Your Score: " , us)
                print("Computer Scor: " , cs)
            else :
                print("Kindly enter the valid guess : ")
    elif i=="N" or i=="n":
        print("Ok GoodBye ):")
        break
    else :
        print("Kindly type the Correct Answer")
    if cs < us:
        print("You won")
    elif cs>us:
        print("Computer won")
    else :
        print("It is a Draw")
exit()