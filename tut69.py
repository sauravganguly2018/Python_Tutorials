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

kundan=Employee("kundan","kumar")
print(kundan.email)
kundan.fname="gunjan"
print(kundan.explain())
print(kundan.email)
kundan.email="ranjan.raj@sauravganguly.com"
print(kundan.email)
del kundan.email
print(kundan.email)
kundan.email="ayush.ranjan@sauravganguly.com"
print(kundan.email)

