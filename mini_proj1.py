# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# SauravLibrary = Library (Listofbooks, library_name)

# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

class Library:
    def __init__(self,booklist,name):
        self.booklist=booklist
        self.name=name
        self.lenddict={}
    def displaybook(self):
        print(f"\nAll available books in our {self.name} library :\b")
        for book in self.booklist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.lenddict and book in self.booklist:
            self.lenddict[book]=user
            self.booklist.remove(book)
            print(f"\n{book} is now given to {user}")
        else:
            if book in self.lenddict:
                print(f"\n{book} is not available because it is lended by {self.lenddict[book]}")
            else:
                print(f"\n{book} is not available in {self.name} Library")
    def addbook(self,book):
        self.booklist.append(book)
        print(f"\n{book} has been added to {self.name} Library")
    def returnbook(self,book):
        if book in self.lenddict:
            self.lenddict.pop(book)
            self.booklist.append(book)
            print(f"\n{book} has been added to {self.name} Library")
        else:
            print(f"\n{book} has not been lended by anyone till now")

if __name__ == '__main__':
    saurav = Library(["c++", "csa", "java", "dsa", "python", "php"], "saurav")
    print("\nWelcome to codewithsaurav Library !")
    choice='y'
    while(choice=="y" or choice=="Y"):
        print("\npress 1 : To display all books ")
        print("press 2 : To lend books")
        print("press 3 : To add book")
        print("press 4 : To return book")
        user_inp=input("Enter your choice : ")
        if user_inp not in ['1','2','3','4']:
            print("\nplease enter a valid option !\n")
            continue
        else:
            user_inp=int(user_inp)
            if user_inp==1:
                saurav.displaybook()
            elif user_inp==2:
                name=input("\nEnter the name of the person who wants to lend a book : ")
                book=input("Enter the name of the book you want to lend : ")
                saurav.lendbook(name,book)
            elif user_inp==3:
                book = input("\nEnter the book you want to add : ")
                saurav.addbook(book)
            else:
                book=input("\nEnter the book you want to return : ")
                saurav.returnbook(book)
            choice=input("\npress y or Y to continue or any other key to exit : ")

