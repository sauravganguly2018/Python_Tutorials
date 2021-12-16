def function_name_print(a,b,c,d):
    print(a,b,c,d)
function_name_print("saurav","kundan","gunjan","ranjan")

def funarg(normal,*args,**kwargs):
    print(type(args))
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is {value}")
lst=["saurav","kundan","gunjan","ranjan"]
lst1={"saurav":"coder","rahul":"web designer","ankit":"income tax officer"}
normal="i am cool"
funarg(normal,*lst,**lst1)
