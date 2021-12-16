# Python Practice Problem 3 (Easy , 15 Points)
# Foods and Calories
#
# You visit a restaurant called Codewithsaurav and food items in this restaurant are sorted based on their
# amount of calories.You have to reverse this list of food items containing their calories.
#
# you have to use following three methods to reverse a list:
# 1. Inbuilt method of python
# 2. Listname[::-1] slicing trick
# 3. Swapping first element with last one and second element with second last one and so on....
#
# Input:
# Take a list as an input from the user
# [5,4,1]
#
# Output:
# [1,4,5]
# [1,4,5]
# [1,4,5]
#
# All the three methods give same results

lst=[4,6,8,10,15,17,20,40,59,70,79]
print(f"List of calories of items in Codewithsaurav restaurant : {lst}")

# Reverse method 1
rev1=lst[:]
rev1.reverse()
print(f"My first reversed list of {lst} is {rev1}")

# Reverse method 2
rev2=lst[::-1]
print(f"My second reversed list of {lst} is {rev2}")

# Reverse method 3
rev3=lst[:]
for i in range(0,len(rev3)//2):
    temp=rev3[i]
    rev3[i]=rev3[len(rev3)-i-1]
    rev3[len(rev3)-i-1]=temp
print(f"My third reversed list of {lst} is {rev3}")

if rev1==rev2 and rev2==rev3:
    print("All the three methods give the same results")

