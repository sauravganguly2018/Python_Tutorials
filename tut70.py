class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@sauravganguly.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is not set. please set it using setter"
        return f"{self.fname}.{self.lname}@sauravganguly.com"

    @email.setter
    def email(self,string):
        print("setting new email...")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

ashish=Employee("ashish","ranjan")
print(type(ashish))
print(type("This is a string"))
print(id(ashish))
print(id("This is a string"))
print(id("That is a string"))

print(dir(ashish))
print(dir("This is me"))

import inspect
print(inspect.getmembers(ashish))