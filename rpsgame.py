import random

sign =['Rock','Paper','Scissors']

Choose=int(input("Enter your choice  Rock Paper Scissors"))
user= sign[Choose]
print("User choose",user)

Comp= random.choice(sign)

print("Computer choose",Comp)

if user == Comp:

    print("It's a tie!")

elif user == "Rock" and Comp == "Scissors":

    print("You win!")

elif user == "Paper" and Comp == "Rock":

    print("You win!")

elif user== "Scissors" and Comp== "Paper":

    print("You win!")
else:
    print("Computer win!")