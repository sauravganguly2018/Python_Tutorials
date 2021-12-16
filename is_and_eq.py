# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object

a=[1,2,3]
b=a
print(a==b)
print(a is b)
c=a[:]
print(a==c)
print(a is c)

# Task :-

g=[6,7,"hj"]
h=[6,7,"hj"]
print(g is h)
