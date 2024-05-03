import requests

url = "http://127.0.0.1:8000/"

data = {
    "unit" : 9000
}

response = requests.post(url, data=data)

print(response.status_code)
print(response.json())
