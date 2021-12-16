class Employee:
    no_of_leaves=10
    var=13

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

class Player:
    var=12
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printplayer(self):
        return f"The name is {self.name}. The game is {self.game}"

class Coolprogrammer(Player,Employee):
    language="java"
    # var=11
    def printlanguage(self):
        print(f"The language is {self.language}")

gunjan=Employee("gunjan",2000000,"daroga")
kundan=Employee.from_str("kundan-10000-student")

saurav=Coolprogrammer("saurav","cricket")
print(saurav.printplayer())
print(saurav.var)
saurav.printlanguage()
