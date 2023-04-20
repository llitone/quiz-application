import requests
from pprint import pprint
# print(requests.post("http://d1ffic00lt.com/app/api/v1.0/authors/", json={"login": "hitler", "password": "fire"}).text)

# print(requests.post("http://d1ffic00lt.com/app/api/v1.0/subjects/", json={"name": "james"}).text)

# print(requests.post("http://d1ffic00lt.com/app/api/v1.0/questions/", json={ "age": 16, "question": "у кого др 20
# апреля?", "difficulty": 1, "value": 10, "subject_id": 1, "explanation": "у гитлера др в этот день", "author_id":
# 1}).text) print(requests.post("http://d1ffic00lt.com/app/api/v1.0/answers/", json={"question_id": 1,
# "answer": "захар", "is_correct": True}).text) print(requests.post("http://d1ffic00lt.com/app/api/v1.0/answers/",
# json={"question_id": 1, "answer": "мама дификульта", "is_correct": True}).text)

pprint(requests.get("http://d1ffic00lt.com/app/api/v1.0/subjects/").json())
