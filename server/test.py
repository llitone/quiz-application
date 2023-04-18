import requests

response = requests.get(
    f"http://127.0.0.1:1238//app/api/v1.0/users/88005553535"
)
print(response.json())

