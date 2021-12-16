var1=5
print("Enter your no. : ",end="")
var2=int(input())

if var1==var2:
    print("equal")
elif var2>var1:
    print("greater")
else:
    print("smaller")

list1=[1,2,3]
print(2 in list1)
print(1 not in list1)

if 2 in list1:
    print("2 is in list1")
if 1 not in list1:
    print("1 is not in list1")

print("Enter your age : ",end="")
age=int(input())
if age<18:
    print("you cannot drive")
elif age==18:
    print("First you come and then we decide you can drive or not")
else:
    print("you can drive")