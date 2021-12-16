# Dictionary is nothing but a key value pair
d1={}
print(type(d1))
d2={"saurav":"intelligent","ram":"dull","shyam":"average","mohan":{"a":1,"b":2,3:4,5:"shakti"}}
print(d2)
print(d2["mohan"])
print(d2["mohan"][5])
print(d2["mohan"]["a"])
d2["kundan"]="funny"
d2[567]="gunjan"
del d2["ram"]
print(d2)

d3=d2  #here d3 is a pointer refering to d2 so any change in d3 will also affect in d2
# d3=d2.copy()
del d3["saurav"]
print(d2)
print(d3)

d2.update({"shivam":"pathak"})
print(d2)
print(d2.keys())
print(d2.items())

