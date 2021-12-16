# Python Practice Problem 6 (Easy, 10 Points)
# Guess The Number
#
# Generate a random integer from a to b. You and your friend have to guess a number between two
# numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will
# have to keep choosing the number and our program must tell whether the number is greater than the
# actual number or less than the actual number. Log the number of trials it took your friend to arrive at the
# number. You play the same game and then the person with minimum number of trials wins !
#
# Randomly generate a number after taking a and b as input and don't show that to the user (say 6)
#
# Input:
# Enter the value of a
# 4
# Enter the value of b
# 13
#
# Output:
# Player1:
# Please guess the number between 4 and 13
# 5
# Wrong guess a greater number again
# 8
# Wrong guess a smaller number again
# 6
# Correct you took 3 trials to guess the number
#
# Player2:
# .
# .
# .
# Correct you took 7 trials to guess the number
# Player 1 wins !

import random

def trials(a,b,act_num):
    print(f"Guess the number between {a} and {b}\n")
    c = 0
    while (True):
        c += 1
        guessed_num = int(input("Guess the number : "))
        if guessed_num == act_num:
            return c
        elif guessed_num > act_num:
            print(f"Wrong guess ! {guessed_num} is greater the actual number")
        else:
            print(f"Wrong guess ! {guessed_num} is smaller the actual number")

if __name__ == '__main__':
    print("<<-------- Guess the number game started -------->>")
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b : "))
    act_num1=random.randint(a+1,b-1)
    act_num2=random.randint(a+1,b-1)
    print("\nPlayer 1 :\n")
    p1=trials(a,b,act_num1)
    print(f"Correct ! Player 1 took {p1} trials to guess the actual number")
    print("\nYou :\n")
    you=trials(a,b,act_num2)
    print(f"Correct ! You took {you} trials to guess the actual number")
    if p1==you:
        print(f"\nGame Draw ! because both of you took {p1} trials to guess the actual number")
    elif p1>you:
        print("\nYou won !")
    else:
        print("\nPlayer 1 won !")
    print(f"\nThe actual number for player 1 was {act_num1} and for you was {act_num2}")
