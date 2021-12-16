l=18

def function1(n):
    # l=3 #Local
    m=15  #Local
    global l
    l=l+10
    print(l,m)
    print(n,"I have printed")

print(l)
function1("Hello")
print(l)

def harry():
    x=20
    def rohan():
        global x
        x=88
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)

harry()
print(x)
