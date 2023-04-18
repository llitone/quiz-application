import requests

while True:
    result = requests.get("http://127.0.0.1:1238")
    print(result)