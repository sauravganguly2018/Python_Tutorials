# Lambda functions or anonymous functions
# minus=lambda x,y:x-y

# def minus(x,y):
#     return x-y
#
# print(minus(7,4))

# def a_first(a):
#     return a[1]

a=[[1,6],[0,9],[1,3],[2,5]]
# a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)