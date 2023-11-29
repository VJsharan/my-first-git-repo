import random
def game():
    you,cpu=0,0
    u=input("Enter your choice: ")
    user=u.lower()
    hands=["rock","paper","scissors","scissor",'papers']
    pc=random.choice(hands)
    if user not in hands:
        print("Invalid choice bro!!")
        u = input("Enter your choice again: ")
    if user==pc:
        print("Tied!")
    elif user=="rock":
        if pc == "scissor":
            print(f"Computer chose {pc}!")
            print("You Win!")
            you+=1
        else:
            print("Computer Wins!")
            cpu += 1
    elif user=="paper":
        if pc=="rock":
            print(f"Computer chose {pc}!")
            print("You Win")
            you += 1
        else:
            print("Computer Wins!")
            cpu += 1
    elif user=="scissor":
            if(pc=="paper"):
                print(f"Computer chose {pc}!")
                print("you win")
                you += 1
            else:
                print("Computer chose rock!")
                print("pc wins")
                cpu+=1
    if you>cpu:
        return print(f"Your score is {you}")
    else:
        return print(f"PC's score is {cpu}")
y=input("Do you want to play? ")
while(y.lower()=="yes" or y.lower()=="yepp"):
    game()
else:
    print("Ok program quitted")
    quit()
