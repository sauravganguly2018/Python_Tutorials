import json

data='{"var1":4,"var2":5}'
print(data)

parsed=json.loads(data)   # used to convert string into dictionary
print(parsed)
print(type(parsed))
print(parsed["var2"])

# Task 1 - json.loads()? karta hai

data2={"var1":2,"jar2":[1,2,3,4,5],"var3":False}
print(data2)
dumped=json.dumps(data2)   # used to convert dictionary into json string
print(dumped)

# Task 2 - what is sort keys parameter in dumps

sort_keys=json.dumps(data2,sort_keys=True)   # used to convert dictionary into json string having sorted keys
print(sort_keys)