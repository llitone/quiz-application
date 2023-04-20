<h1 align="center">API</h1>


# v1.0
## 1. Обзор

API для связи клиента и сервера

## 1.1 Users

### POST
#### Пример запроса в формате json
```python
{
    "name": {name}, 
    "age": {age}, 
    "phone_number": {phone_number}, 
    "password": {password}, 
    "points": {points}
}
```
#### Пример запроса
```python
import requests

json = {
    "name": {name}, 
    "age": {age}, 
    "phone_number": {phone_number}, 
    "password": {password}, 
    "points": {points}
}

requests.post("http://{host}/app/api/v1.0/users/", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса
```python
import requests

requests.get("http://{host}/app/api/v1.0/users/<phone>")
```
#### Ответ
```python
{
    "id": {id},
    "name": {name},
    "age": {age},
    "phone_number": {phone_number},
    "password": {password},
    "points": {points}
}
```

## 1.3 Answers

### POST
#### Пример запроса в формате json
```python
{
    "question_id": {question_id}, 
    "answer": {answer}, 
    "is_correct": {is_correct}
}
```
#### Пример запроса
```python
import requests

json = {
    "question_id": {question_id}, 
    "answer": {answer}, 
    "is_correct": {is_correct}
}

requests.post("http://{host}/app/api/v1.0/answers/", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET

#### Пример запроса
```python
import requests

requests.get("http://{host}/app/api/v1.0/answers/<int:question_id>")
```
#### Ответ
```python
{
    "id": {id},
    "question_id": {question_id},
    "answer": {answer},
    "is_correct": {is_correct}
}
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://127.0.0.1:5000/app/api/v1.0/answers/<int:question_id>")
```

#### Ответ
```python
{
    "success": True
}
```
## 1.4 Questions

### POST
#### Пример запроса в формате json
```python
{
    "age": {age}, 
    "question": {question}, 
    "difficulty": {difficulty}, 
    "value": {value},
    "subject_id": {subject_id}, 
    "explanation": {explanation}, 
    "author_id": {author_id}
}
```
#### Пример запроса
```python
import requests

json = {
    "age": {age}, 
    "question": {question}, 
    "difficulty": {difficulty}, 
    "value": {value},
    "subject_id": {subject_id}, 
    "explanation": {explanation}, 
    "author_id": {author_id}
}

requests.post("http://{host}/app/api/v1.0/questions/", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса для одного question
```python
import requests

requests.get("http://{host}/app/api/v1.0/questions/<int:question_id>")
```
#### Ответ
```python
{
    "id": {id},
    "age": {age},
    "question": {question},
    "difficulty": {difficulty},
    "value": {value},
    "subject_id": {subject_id},
    "explanation": {explanation}, 
    "author_id": {author_id}
}
```
#### Пример запроса для всех questions
```python
import requests

requests.get("http://{host}/app/api/v1.0/questions/")
```
#### Ответ
```python
{
    {subject}: [
        {
            "id": {question_id},
            "age": {question_age},
            "question": {question_question},    
            "difficulty": {question_difficulty},
            "value": {question_value},
            "subject_id": {question_subject_id},
            "explanation": {question_explanation}, 
            "author_id": {author_id},
            "answers": [
                {
                    "id": {answer_id},
                    "question_id": {answer_question_id},
                    "answer": {answer_answer},
                    "is_correct": {answer_is_correct}
                }
            ]
        }
    ]
}
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://127.0.0.1:5000/app/api/v1.0")
```

#### Ответ
```python
{
    "success": True
}
```
## 1.5 Subjects

### POST
#### Пример запроса в формате json
```python
{
    "name": {name}
}
```
#### Пример запроса
```python
import requests

json = {
    "name": {name}
}

requests.post("http://{host}/app/api/v1.0/subjects/", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса
```python
import requests

requests.get("http://{host}/app/api/v1.0/subjects/")
```
#### Ответ
```python
[
    {
        "id": {id},
        "subject": {subject}
    }
]
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://127.0.0.1:5000/app/api/v1.0/subjects/")
```

#### Ответ
```python
{
    "success": True
}
```
## 1.6 Quizzes

### POST
#### Пример запроса в формате json
```python
{
    "room_id": {room_id}
}
```
#### Пример запроса
```python
import requests

json = {
    "room_id": {room_id}
}

requests.post("http://{host}/app/api/v1.0", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса
```python
import requests

requests.get("http://{host}/app/api/v1.0")
```
#### Ответ
```python
{
    "id": {id}, 
    "room_id": {room_id}, 
    "start_at": {start_at}
    }
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://127.0.0.1:5000/app/api/v1.0")
```

#### Ответ
```python
{
    "success": True
}
```
## 1.7 Quiz Questions

### POST
#### Пример запроса в формате json
```python

```
#### Пример запроса
```python
import requests

json = {
    
}

requests.post("http://{host}/app/api/v1.0", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса
```python
import requests

requests.get("http://{host}/app/api/v1.0")
```
#### Ответ
```python
{
    
}
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://127.0.0.1:5000/app/api/v1.0")
```

#### Ответ
```python
{
    "success": True
}
```
