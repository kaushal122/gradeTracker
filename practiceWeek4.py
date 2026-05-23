import requests
from dotenv import load_dotenv
import os
response=requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)
data=response.json()
#print(type(data))
#print(data)
for d in data:
    print(d["name"]," --- ",d["email"])

response2=requests.get("https://jsonplaceholder.typicode.com/users/1")
data1=response2.json()
print(data1)
print(data1["name"], data1["email"],data1["address"]["city"])
#print(data==data1)

load_dotenv()
key=os.getenv("MY_API_KEY")
print(key)
data2={
    "title":" my first post",
    "body":"Hello World",
    "id":1
}
post=requests.post("https://jsonplaceholder.typicode.com/posts",json=data2)
print(post.json())