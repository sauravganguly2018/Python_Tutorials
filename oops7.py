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

    @classmethod         # acting as an alternative constructor
    def from_str(cls,string):
        return cls(*string.split("-"))  # one liner

    @staticmethod
    def printgood(string):
        print("This is good "+string)

    pass

class Programmer(Employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=alanguages

    def printprog(self):
        return f"The programmer's name is {self.name}. The salary is {self.salary} and the role is {self.role}" \
               f" and the languages is {self.language}"

gunjan=Employee("gunjan",2000000,"daroga")
kundan=Employee.from_str("kundan-10000-student")

saurav=Programmer("saurav",30000000,"programmer",["c++","java","python","java script"])
print(saurav.printprog())