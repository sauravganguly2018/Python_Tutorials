# Health Management System

def getdate():
    import datetime
    return datetime.datetime.now()

def log(file_name,work):
    with open(file_name,"a") as f:
        f.write(work+"\n")

def retrieve(file_name):
    with open(file_name) as f:
        for line in f:
            print(line,end="")

def name(name1):
    choice2=int(input("press 1 for food and 2 for exercise : "))
    if choice2==1:
        choice3=int(input("press 1 for log and 2 for retrieve : "))
        if choice3==1:
            work=input("Enter the food : ")
            time=getdate()
            food="[ "+str(time)+" ] "+work
            log(name1+"_food.txt",food)
        elif choice3==2:
            retrieve(name1+"_food.txt")
        else:
            print("Invalid choice !")
    elif choice2==2:
        choice3=int(input("press 1 for log and 2 for retrieve : "))
        if choice3==1:
            work=input("Enter the exercise name : ")
            time=getdate()
            exercise="[ "+str(time)+" ] "+work
            log(name1+"_exercise.txt",exercise)
        elif choice3==2:
            retrieve(name1+"_exercise.txt")
        else:
            print("Invalid choice !")
    else:
        print("Invalid Input !")

person_name={1:"saurav",2:"kundan",3:"gunjan"}
for key,value in person_name.items():
    print("press",key,"for",value)
choice1=int(input("Type your choice : "))
try:
    name(person_name[choice1])
except Exception as e:
    print("Invalid Input !")
