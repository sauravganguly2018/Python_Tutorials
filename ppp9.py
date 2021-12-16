import random

n=int(input("Enter the number of names : "))

name_lst=[]
for i in range(n):
    name=input(f"Enter name{i+1} : ")
    name_lst.append(name)
# print(name_lst)

name_lst1=[item.split() for item in name_lst]
name_lst2=[]
for i in range(len(name_lst1)):
    if len(name_lst1[i]) > 2:
        for j in range(2, len(name_lst1[i])):
            name_lst1[i][1] +=" "+name_lst1[i][2]
            name_lst1[i].remove(name_lst1[i][2])
    name_lst2.append(name_lst1[i])

# print(name_lst2)

for i in range(len(name_lst2)):
    ran1=random.randint(0,len(name_lst2)-1)
    ran2=random.randint(0,len(name_lst2)-1)
    temp=name_lst2[ran1][0]
    name_lst2[ran1][0]=name_lst2[ran2][0]
    name_lst2[ran2][0]=temp

for i in range(len(name_lst2)):
    ran1=random.randint(0,len(name_lst2)-1)
    ran2=random.randint(0,len(name_lst2)-1)
    temp=name_lst2[ran1][1]
    name_lst2[ran1][1]=name_lst2[ran2][1]
    name_lst2[ran2][1]=temp

# print(name_lst2)
for i in range(len(name_lst2)):
    print(f"{name_lst2[i][0]} {name_lst2[i][1]}")