# pattern printing
# Input = Integer n
# Boolean = True or False
#
# True n=4
# *
# **
# ***
# ****
#
# False
# ****
# ***
# **
# *

inp1=int(input("Enter the number of rows : "))
inp2=int(input("Enter the boolean value : "))
if inp2==True:
    i=0;
    while i<inp1:
        j=0
        while j<i+1:
            print("*",end="")
            j+=1
        print()
        i+=1
else:
    i=0
    while i<inp1:
        j=0
        while j<inp1-i:
            print("*",end="")
            j += 1
        print()
        i += 1