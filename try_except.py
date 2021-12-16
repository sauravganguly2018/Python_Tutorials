print("Enter num 1 : ")
inp1=input()
print("Enter num 2 : ")
inp2=input()

try:
    print("The sum of these two numbers is : ",int(inp1)+int(inp2))
except Exception as e:
    print(e)

print("This is a very important statement to be printed")
