# Email Collector
# str='''
# '''
# email1
# email2
# email3

import re
str='''saurav@co.in
kundan@gmail.com
hgfdhjgfhjd gdh@hfd.djkh gfghf
ghghjg@hgfhg
hgfh@hfj.bjh.ibkh
'''
emails=re.findall("\w+@[a-zA-Z]+[.][A-Za-z]+",str)
print(emails)