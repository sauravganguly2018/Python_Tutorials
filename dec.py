# def function1():
#     print("Subscribe Now !")
#
# func2=function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=funcret(1)
# print(a)

# def executor(func):
#     func("hello saurav")
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_saurav():
    print("Saurav is a good boy")

# w=dec1(who_is_saurav)
# w()

who_is_saurav()