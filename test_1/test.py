import requests
import json

url = "http://127.0.0.1:8000"

name = "bridge"
path = "./bridge.jpg"

data = {
    "name" : name,
    "img" : path
}

response = requests.post(url,data=data)

print(response.text())
