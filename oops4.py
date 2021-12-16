class Employee:
    no_of_leaves=10

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name}. The salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leaves=leaves
    pass


gunjan=Employee("gunjan",2000000,"daroga")
# Employee.change_leaves(100) - This is also valid
gunjan.change_leaves(100)
print(gunjan.printdetails())
print(gunjan.no_of_leaves)