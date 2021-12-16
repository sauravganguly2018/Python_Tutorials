# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls=[i for i in range(100) if i%3==0 ]
# print(ls)

# dict1={i:f"item{i}" for i in range(4,30) if i%3==0}
# dict2={value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)

# dresses={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]}
# print(type(dresses))
# print(dresses)

evens=(i for i in range(100) if i%2==0)
print(type(evens))
print(evens)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

for item in evens:
    print(item)
