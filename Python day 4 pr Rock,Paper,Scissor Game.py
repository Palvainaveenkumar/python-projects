import random
print("Welcome To Rock Paper Scissor Game....!")
option=int(input("What do you choose ? 0 for Rock , 1 For Paper , 2 for Scissor..enter your option "))
print("your option is :",option)
l=[0,1,2]
system=random.choice(l)
computer=system
print("computer option is :",computer)
if option==0 and computer==0:
    print("Draw try again")
elif option==0 and computer==1:
    print("computer win you loose")
elif option==0 and computer==2:
    print("computer loose & you own")
elif option==1 and computer==0:
    print("you win computer loose")
elif option==1 and computer==1:
    print("Draw Try again")
elif option==1 and computer==2:
    print("you loose & computer win")
elif option==2 and computer==0:
    print("you loose & computer win")
elif option==2 and computer==1:
    print("you win & computer loose")
elif option==2 and computer==2:
    print("Draw Try again")
else:
    print("invalid input")