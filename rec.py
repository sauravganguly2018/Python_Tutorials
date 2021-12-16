def print2(str1):
    # print2(str1)
    print("This is",str1)

print2("saurav")

def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

def factorial_recursive(n):
    if n==0:
        return 1
    return n*factorial_recursive(n-1)

def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n1=int(input("Enter the no. : "))
print("factorial using iterative approach is : ",factorial_iterative(n1))
print("factorial using recursive approach is : ",factorial_recursive(n1))
n2=int(input("Enter the index of fibonacci sequence : "))
print("fibonacci sequence of given index is : ",fibonacci(n2))

