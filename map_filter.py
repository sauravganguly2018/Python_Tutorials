# *****************************MAP************************************
# lst=["34","78","89"]
#
# for i in range(len(lst)):
#     lst[i]=int(lst[i])
#
# lst[2]=lst[2]+1
# print(lst[2])

# lst2=["56","98","23","54","2"]
# lst3=list(map(int,lst2))
# print(lst3)

# def sq(a):
#     return a*a
# num=[1,2,3,4,5,6]
# num=list(map(sq,num))
# square=list(map(lambda x:x*x,num))
# print(square)

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func=[square,cube]
#
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)

# *****************************FILTER*********************************

lst4=[1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5=list(filter(is_greater_5,lst4))
print(gr_than_5)

# *****************************REDUCE*********************************
from functools import reduce

lst5=[3,4,5,6,2]
num=reduce(lambda x,y:x*y,lst5)

# num=0
# for i in lst5:
#     num+=i
print(num)


