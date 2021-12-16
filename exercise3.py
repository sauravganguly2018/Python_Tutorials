n=18

#no of guesses 9
#no of guesses left
#no of guesses he took to finish
#game over

guesses=9
flag=False
while(guesses!=0):
    print("you have",guesses,"guesses remaining :\nGuess the number : ")
    num=int(input())
    if num==n:
        flag=True
        break
    elif num<n:
        print("no. is lesser\n")
        guesses-=1
    else:
        print("no. is greater\n")
        guesses-=1

if flag:
    print("you got the correct guess !")
    print("you took ",10-guesses,"guesses to win the game")
else:
    print("Game Over !")