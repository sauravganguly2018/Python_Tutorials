class Employee:
    no_of_leaves=10
    _protec=20
    __privat=67

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name}. The salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leaves=leaves

    @classmethod         # acting as an alternative constructor
    def from_str(cls,string):
        return cls(*string.split("-"))  # one liner

    @staticmethod
    def printgood(string):
        print("This is good "+string)

saurav=Employee("saurav",10000000,"programmer")
print(saurav._protec)
print(saurav._Employee__privat)  # name angling