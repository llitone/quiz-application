from pprint import pprint

import requests

result = requests.post("http://d1ffic00lt.com/app/api/v1.0/users/", json={
"name": "ШУШНОВ САША",
            "age": 11,
            "phone_number": "88009999999",
            "password": "1234567890",
            "points": 0

})
print(result)
