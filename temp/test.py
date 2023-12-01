
import requests
import json

url1 ="http://127.0.0.1:8000/isPrime/"

for i in range(0,100):
    r1 = requests.get(url1+f"{i}")
    data = json.loads(r1.text)
    if data["IsPrime"] == "True":
        print(f"Number = {data['Number']}")