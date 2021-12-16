import requests
r=requests.get("https://codewithharry.com")
print(r.text)
print(r.status_code)

# url="www.something.com"
# data={"p1":2,"p2":9}
# r2=requests.post(url=url,data=data)
