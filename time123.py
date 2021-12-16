import time

initial=time.time()
k=0
while(k<10):
    print("hello saurav")
    time.sleep(2)
    k+=1

print("while loop takes ",time.time()-initial,"sec")

initial2=time.time()
# print(initial2)
for i in range(10):
    print("hello kundan")
print("for loop takes ",time.time()-initial2,"sec")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)