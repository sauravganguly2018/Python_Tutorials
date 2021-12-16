"""
Iterable - __iter() or __getitem__()
Iterator - __next__()
Iteration -
"""

def gen1(n):    # It is an Iterator which traverses only once
    for i in range(n):
        yield i

g=gen1(4)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())   # It should not be run more than 4 times

for i in g:
    print(i)

s="saurav"     # s=46578 is not iterable because s is int here in this case
ier=iter(s)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# for c in s:
#     print(c)