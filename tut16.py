list1=[["saurav",1],["kundan",2],["gunjan",3]]
for item,num in list1:
    print(item," having number :",num)
dict1=dict(list1)
for item in dict1:
    print(item)
for item,num in dict1.items():
    print(item," having number :",num)
list2=[int,"kundan",float,3,14,7,2,9,8,1,0,10]
for item in list2:
    if str(item).isnumeric() and item>6:
        print(item)