class Employee:
    no_of_leaves=10
    pass

saurav=Employee()
kundan=Employee()

saurav.name="saurav"
saurav.role="Instructor"
saurav.salary=10000000

kundan.name="kundan"
kundan.salary=1000000
kundan.role="student"

print(Employee.no_of_leaves)
print(saurav.no_of_leaves)
saurav.no_of_leaves=30 # - it will not change the value of class variable . it will create a new variable
# of that name for that object only
Employee.no_of_leaves=20
print(Employee.no_of_leaves)
print(saurav.no_of_leaves)
print(kundan.no_of_leaves)
print(kundan.role)
print(saurav.role)
print(kundan.__dict__)
print(saurav.__dict__)
print(Employee.__dict__)