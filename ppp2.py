# Python practice problems 2 (Easy , 10 points)
# Divide The Apples
#
# Harry Potter has got n numbers of apple, Harry has some students among whom, he wants to distribute the
# apples . These n numbers of apples are provided to harry by his friends and he can request for few more or few
# less apples
# you need to print whether a number in range min to max is a divisor of n or not
#
# Input
# Take input n mn and mx from the user
#
# Output
# print whether the numbers between mn and mx are divisor of n or not
#
# Example
# if n is 20 and mn=2 and mx=5
# 2 is divisor of 20
# 3 is not divisor of 20
# ...
# 5 is a divisor of 20
try:
    n=int(input("Enter the numbers of apples Harry wants to input : "))
    mn=int(input("Enter the min value for divisor : "))
    mx=int(input("Enter the max value for divisor : "))
except Exception as e:
    print("Enter Integers only !")
    exit()
if mx>=mn:
    if mn==mx:
        res=n%mn
        print(f"This is not a range and the result for the number is : {res} ")
        if res == 0:
            print(f"{mn} is divisor for {n}")
        else:
            print(f"{mn} is not a divisor of {n}")
    else:
        for i in range(mn,mx+1):
            res=n%i
            if res==0:
                print(f"{i} is divisor for {n}")
            else:
                print(f"{i} is not a divisor of {n}")
else:
    print("you entered value of mn greater than mx . That is not possible ! ")




