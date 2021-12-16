import os

print(dir(os))
print(os.getcwd())
# os.chdir("c://")
# print(os.getcwd())
# open("saurav.txt")  # It will give an error because the present working directory changed to c:/ folder
print(os.listdir())
print(os.listdir("c://"))
print(type(os.listdir("c://")))
# os.mkdir("this")
# os.makedirs("this/that")
# os.rename("kundan.txt","gunjan.txt")
print(os.environ.get("Path"))
print(os.path.join("c://", "saurav.txt"))
print(os.path.exists("c://"))
print(os.path.exists("c://saurav"))
print(os.path.isdir("c://Program Files"))
print(os.path.isfile("c://Program Files"))
print(os.path.isfile("D:\Pictures\Screenshots/1.jpg"))
for item in os.listdir("D:/saurav"):
    i=1
    if item.endswith(".txt"):
        print(item)
        os.rename(item,f"{i}.txt")
        i+=1
