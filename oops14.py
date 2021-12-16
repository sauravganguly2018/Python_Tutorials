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

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee ('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return f"The name is {self.name}. The salary is {self.salary} and the role is {self.role}"

emp1=Employee("saurav",444,"programmer")
emp2=Employee("kundan",555,"railway engineer")

print(emp1+emp2)
print(emp1/emp2)
print(repr(emp1))
print(str(emp1))
print(emp1)   # By default str is called