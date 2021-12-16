# a=3
# b=5
# c=sum((a,b))
# print(c)

def function1(a,b):
    print("Hello you are in function 1 : ",a*b)
def function2(a,b):
    """This is a function which will calculate the average of two numbers
       This function doesn't work for three numbers"""
    average=(a+b)/2
    return average

function1(3,6)
print(function2.__doc__)
avg=function2(9,7)
print(avg)
