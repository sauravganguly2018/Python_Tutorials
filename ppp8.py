# Python Practice Problem 8(Easy, 10 Points)
# Rohan Das is a fraud
# Rohan Das wrote a python function to print a multiplication table of a given number and put one of the
# values(randomly generated) as a wrong.
# Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate
# this!
# So you decided to use your python skills to counter Rohan's actions by writing a python program that
# validates Rohan's multiplication table
# Your function should be able to find out the wrong values in Rohan's table and expose Rohan Das as a
# fraud.
# Note: Rohan's function returns a list of numbers like this
#
# Rohan Das's Function Input:
# rohanMultiplication(6)
#
# Rohan's Function returns this output:
# [6,12,18,26,....,60]
#
# You have to write a function isCorrect(table,number) and return the index where rohan's function is wrong
# and print it to the screen! if the table is correct, your function returns None.

import random

def rohanMultiplication(num):
    ran=random.randint(2,9)
    lst=[num*i if i!=ran else random.randint(num*(i-1),num*(i+1)) for i in range(1,11) ]
    return lst

def isCorrect(table,num):
    for i in range(1,11):
        if num*i!=table[i-1]:
            return i
    return -1

if __name__ == '__main__':
    num=int(input("Enter the number to get the table : "))
    table=rohanMultiplication(num)
    print(f"Rohan Das' table is : {table}")
    check=isCorrect(table,num)
    if check!=-1:
        print(f"Rohan Das' table is false at an index {check}")
    else:
        print("Rohan Das' table is true")

