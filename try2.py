f1=open("saurav.txt")
try:
    f2=open("does.txt")

except EOFError as e:
    print("EOFError has come ",e)

except IOError as e:
    print("IOError has come ",e)

else:
    print("Except statement is not run")

finally:
    print("This is finally block to be executed at any cost")
    f1.close()

print("Important message")