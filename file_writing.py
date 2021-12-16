# f=open("saurav2.txt","w")
# a=f.write("saurav is awesome !\n")
# print(a)

# f=open("saurav2.txt","a")
# a=f.write("saurav is a charmish boy !\n") # It prints no. of characters appended to a file
# print(a)

# Handle read and write both
f=open("saurav2.txt","r+")
print(f.read())
f.write("Thank you bhai !\n")
f.close()