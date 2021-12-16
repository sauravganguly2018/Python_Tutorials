# a=input("Enter your name : ")
# b=input("How much do you earn : ")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")

# 10000 lines taking 1 hour

# Task write about 2 built in exception

c=input("Enter your name : ")
try:
    print(a)
except Exception as e:
    if c=="saurav":
        raise ValueError("saurav is blocked in ur company")
    print("Exception handled")
