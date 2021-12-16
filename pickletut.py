import pickle

# car=["Lamborgini","ferrari","tesla","bmw","suzuki"]
file="mypickle.pkl"
# fileobj=open(file,"wb")
# pickle.dump(car,fileobj)
# fileobj.close()

fileobj2=open(file,"rb")
mycar=pickle.load(fileobj2)
print(mycar)
print(type(mycar))
fileobj2.close()

# pickle.loads = ?
