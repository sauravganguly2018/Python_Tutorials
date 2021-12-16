class Employee:
    no_of_leaves=10

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name}. The salary is {self.salary} and the role is {self.role}"
    pass

# saurav=Employee()
# kundan=Employee()
#
# saurav.name="saurav"
# saurav.role="Instructor"
# saurav.salary=10000000
#
# kundan.name="kundan"
# kundan.salary=1000000
# kundan.role="student"

# print(saurav.printdetails())

gunjan=Employee("gunjan",2000000,"daroga")
print(gunjan.printdetails())

