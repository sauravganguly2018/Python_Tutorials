# pickle
# Use requests module to download the iris dataset
import requests
import pickle
r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
lst=[item.split(",") for item in r.split("\n") if len(item)!=0]

with open("iris.pkl","wb") as f:
    pickle.dump(lst,f)

with open("iris.pkl","rb") as f:
    print(pickle.load(f))
