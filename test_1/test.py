import requests
import json

url = "http://127.0.0.1:8000"

name = "bridge"
path = "./bridge.jpg"

data = {
    "user" : "give me python code for addition of 2 number"
}

response = requests.post(url,json=data)

print(response.text)
