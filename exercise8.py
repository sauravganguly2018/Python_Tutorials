# Oh soldier Prettify my Folder

# path,dictionary file,format
import os

def rename_file(path):
    os.chdir(path)
    i=1
    for item in os.listdir(path):
            if item.endswith(".jpg"):
                os.rename(item,f"{i}.jpg")
                i+=1
            elif item.endswith(".pdf"):
                os.rename(item, f"{item[0].upper()}{item[1:len(item)]}.pdf")
            elif item.endswith(".txt"):
                os.rename(item, f"{item[0].upper()}{item[1:len(item)]}.txt")
            else:
                pass

rename_file("D:/saurav")
