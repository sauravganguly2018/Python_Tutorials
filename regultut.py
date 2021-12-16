import re

str1='''hello google
how are you? 67897-6756
are you fine savavuravvvhvvvvv now
'''

# Meta Characters

# patt=re.compile(r'are')
# patt=re.compile(r'.')
# patt=re.compile(r're')
# patt=re.compile(r'.re')
# patt=re.compile(r'^hello')
# patt=re.compile(r'ow$')
# patt=re.compile(r'av*')
# patt=re.compile(r'a*v*')
# patt=re.compile(r'av+')
# patt=re.compile(r'av{2}')
# patt=re.compile(r'(av){2}|av{2}')

# Special Sequences

# patt=re.compile(r'\Ahello')
# patt=re.compile(r're\b')
# patt=re.compile(r're\b')
# patt=re.compile(r'\d{2}')
patt=re.compile(r'\d{5}-\d{4}')

matches=patt.finditer(str1)
matches=patt.finditer(str1)

for match in matches:
    print(match)

# Task
# Given a string with a lot of indian phone numbers starting from +91

str2='''+91-6876876782
+91-6276786870 sgjh
+91-7878978
'''

patt2=re.compile(r'\+91-\d{10}')
matches2=patt2.finditer(str2)
lst=[]

for match2 in matches2:
    lst.append(str2[match2.span()[0]:match2.span()[1]])
print(lst)
