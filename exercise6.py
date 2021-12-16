# snake water gun
import random
ch='y'
while(ch=='y' or ch=='Y'):
    i=1
    comp_p = 0
    user_p = 0
    while(i<=10):
        print(f"\nRound {i} start !")
        print("press 1 for snake\npress 2 for water\npress 3 for gun")
        choice=int(input("Type your choice : "))
        lst=["snake","water","gun"]
        comp=random.choice(lst)
        if choice==1:
            if comp=="snake":
                comp_p+=1
                user_p+=1
                print(f"Tie\nYou have {user_p} points and computer has {comp_p} points")
            elif comp=="water":
                user_p+=1
                print(f"you won\nYou have {user_p} points and computer has {comp_p} points")
            else:
                comp_p+=1
                print(f"computer won\nYou have {user_p} points and computer has {comp_p} points")
        elif choice==2:
            if comp=="snake":
                comp_p+=1
                print(f"computer won\nYou have {user_p} points and computer has {comp_p} points")
            elif comp=="water":
                comp_p+=1
                user_p+=1
                print(f"Tie\nYou have {user_p} points and computer has {comp_p} points")
            else:
                user_p+=1
                print(f"you won\nYou have {user_p} points and computer has {comp_p} points")
        elif choice==3:
            if comp=="snake":
                user_p+=1
                print(f"you won\nYou have {user_p} points and computer has {comp_p} points")
            elif comp=="water":
                comp_p+=1
                print(f"computer won\nYou have {user_p} points and computer has {comp_p} points")
            else:
                comp_p+=1
                user_p+=1
                print(f"Tie\nYou have {user_p} points and computer has {comp_p} points")
        else:
            print("Invalid Input Given !")
            i-=1
        i+=1
    print(f"Final score of your's is {user_p} and computer is {comp_p}\n")
    if comp_p==user_p:
        print("game draw")
    elif comp_p>user_p:
        print("computer won the game")
    else:
        print("you won the game")
    ch=input("Do you want to play again ?(y/n) : ")
