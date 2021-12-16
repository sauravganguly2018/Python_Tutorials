# Python Practice Problem 7 (Medium, 20 Points)
# Search Engine
# You are given few sentences as a list (Python list of sentences). Take a query string as an input from the
# user.You have to pull out the sentences matching this query inputted by the user in decreasing order of
# relevance after converting every word in the query and the sentence to lowercase.Most relevant
# sentence is the one with the maximum number of matching words with the query.
#
# Sentences=["This is good","Python is good","Python is not snake"]
#
# Input :
# Please input your query string
# "Python is"
#
# Output :
# 3 results found
# 1. Python is not Python snake
# 2. Python is good
# 3. This is good

sentences=["This is good","Python is good","Python is not snake"]
a=[items.split() for items in sentences]
user_inp=input("Please enter your query string : ")
user_inp_lst=user_inp.split()
occur_dict={}
# print(user_inp_lst)
for i in range(len(a)):
    occur_dict[i]=0
    for k in range(len(user_inp_lst)):
        for j in range(len(a[i])):
            if user_inp_lst[k].lower()==a[i][j].lower():
                occur_dict[i]+=1
c=0
for i in range(len(a)):
    if occur_dict[i]>0:
        c+=1
print(f"{c} results found !")

sorted_values=sorted(occur_dict.values(),reverse=True)
# sorted_values.reverse()
# print(sorted_values)
desc_dict={}

for items in sorted_values:
    for i in occur_dict.keys():
        if items==occur_dict[i]:
            desc_dict[i]=items
            occur_dict.pop(i)
            break
num=1
for items in desc_dict.keys():
    if desc_dict[items]>0:
        print(f"{num}. \"{sentences[items]}\" : with a score of {desc_dict[items]}")
        num+=1
    else:
        break
