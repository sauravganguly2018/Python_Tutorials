def searcher():
    import time
    # some 4 seconds time consuming task
    book="This is a book written by saurav and you can buy this on amazon"
    time.sleep(4)

    while True:
        text=(yield )
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")

search=searcher()
print("search started")
next(search)
print("next method run")
search.send("saurav")
input("Enter any key : ")
search.send("amazon is")
search.close()

# search.send("amazon")   # this will throw the error because search method has closed already
