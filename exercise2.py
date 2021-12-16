# Exercise 2 - Faulty Calculator
# 45*3=555, 56+9=77,56/6=4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45*3=555, 56+9=77,56/6=4
# Your program should take operator and the two numbers as input from the user
# and then return the result
inpu="y"
while(inpu=="y" or inpu=="Y"):
    inp1=int(input("Enter the first number : "))
    inp2=int(input("Enter the second number : "))
    print("Which operations do you want to perform ? : + , - , * , /")
    inp=input("Enter the operator of your choice : ")
    if inp=="+":
        if (inp1==56):
            if(inp2==9):
                print("77")
        elif (inp1==9):
            if (inp2==56):
                print("77")
        else:
            print(inp1+inp2)
    elif inp=="-":
            print(inp1-inp2)
    elif inp=="*":
        if (inp1==45):
            if(inp2==3):
                print("555")
        elif (inp1==3):
            if (inp2==45):
                print("555")
        else:
            print(inp1*inp2)
    elif inp=="/":
        if (inp1==56):
            if (inp2 == 6):
                print("4")
        elif (inp1 == 6):
            if (inp2 == 56):
                print("4")
        else:
            print(inp1/inp2)
    else:
        print("Invalid Input Given !")
    inpu=input("Press Y or y to continue or any other key to exit : ")

