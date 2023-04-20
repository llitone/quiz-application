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
`name` - имя пользователя.<br>
`age` - возраст пользователя.<br>
`phone_number` - номер телефона (логин) пользователя.<br>
`password` - хэшированный пароль пользователя.<br>
`points` - количество очков пользователя.<br>

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

`name` - имя пользователя.<br>
`age` - возраст пользователя.<br>
`phone_number` - номер телефона (логин) пользователя.<br>
`password` - хэшированный пароль пользователя.<br>
`points` - количество очков пользователя.<br>


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
`<phone>` - номер телефона (логин) пользователя. <br>
`id` - id пользователя.<br>
`name` - имя пользователя.<br>
`age` - возраст пользователя.<br>
`naphone_number` - номер телефона (логин) пользователя.<br>
`password` - хэшированный пароль пользователя.<br>
`points` - количество очков пользователя.<br>
## 1.2 Answers

### POST
#### Пример запроса в формате json
```python
{
    "question_id": {question_id}, 
    "answer": {answer}, 
    "is_correct": {is_correct}
}
```
`question_id` - id вопроса, к которому привязан ответ.<br>
`answer` - ответ на вопрос.<br>
`is_correct` - корректность вопроса.<br>
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
`question_id` - id вопроса, к которому привязан ответ.<br>
`answer` - ответ на вопрос.<br>
`is_correct` - корректность ответа.<br>
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
`<int:question_id>` - id вопроса. <br>
`id` - id ответана вопрос. <br>
`question_id` - id вопроса, к которому привязан ответ.<br>
`answer` - ответ на вопрос.<br>
`is_correct` - корректность ответа.<br>
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://{host}/app/api/v1.0/answers/<int:question_id>")
```
`<int:question_id>` - id вопроса. <br>

#### Ответ
```python
{
    "success": True
}
```
## 1.3 Questions

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
`age` - возраст целевой аудитории.<br>
`question` - вопрос.<br>
`difficulty` - сложность вопроса.<br>
`value` - кличество очков за правильный ответ.<br>
`subject_id` - id предмета, к которому привязан вопрос.<br>
`explanation` - объеснение ответа на вопрос.<br>
`author_id` - id автора вопроса.<br>

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
`age` - возраст целевой аудитории.<br>
`question` - вопрос.<br>
`difficulty` - сложность вопроса.<br>
`value` - кличество очков за правильный ответ.<br>
`subject_id` - id предмета, к которому привязан вопрос.<br>
`explanation` - объеснение ответа на вопрос.<br>
`author_id` - id автора вопроса.<br>
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
`<int:question_id>` - id вопроса. <br>
`id` - id вопроса. <br>
`age` - возраст целевой аудитории.<br>
`question` - вопрос.<br>
`difficulty` - сложность вопроса.<br>
`value` - кличество очков за правильный ответ.<br>
`subject_id` - id предмета, к которому привязан вопрос.<br>
`explanation` - объеснение ответа на вопрос.<br>
`author_id` - id автора вопроса.<br>
#### Пример запроса для всех questions
```python
import requests

requests.get("http://{host}/app/api/v1.0/questions/")
```
#### Ответ
```python
[
    {
        "id": {subject_id},
        "subject": {subject_subject},
        "questions": [
            {
                "age": {question_age},
                "author_id": {question_author_id},
                "difficulty": {question_difficulty},
                "explanation": {question_explanation},
                "id": {question_id},
                "question": {question_question},
                "subject_id": {question_subject_id},
                "value": {question_value},
                "answers": [
                    {
                        "answer": {answer_answer},
                        "id": {answer_id},
                        "is_correct": {answer_is_correct},
                        "question_id": {answer_question_id}
                    }
                ]
            }
        ]
    }
]
```
`subject_id` - id предмета, к которому привязан вопрос. <br>
`subject_subject` - название предмета, к которому привязан вопрос.  <br>
`question_age` - возраст целевой аудитории вопроса.  <br>
`question_author_id` - id автора вопроса. <br>
`question_difficulty` - уровень сложности вопроса. <br>
`question_explanation` - объеснения.  <br>
`question_id` - id вопроса.  <br>
`question_question` - вопрос. <br>
`question_subject_id` - id предмета, к которому привязан вопрос. <br>
`question_value` - кличество очков за правильный ответ.  <br>
`answer_answer` - ответ на вопрос. <br>
`answer_id` - id ответа на вопрос. <br>
`answer_is_correct` - корректность ответа на вопрос. <br>
`answer_question_id` - id вопроса, привязанного к ответу. <br>
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://{host}/app/api/v1.0/questions/<int:question_id>")
```
`<int:question_id>` - id вопроса. <br>

#### Ответ
```python
{
    "success": True
}
```
## 1.4 Subjects

### POST
#### Пример запроса в формате json
```python
{
    "name": {name}
}
```
`name` - название предмета. <br>

#### Пример запроса
```python
import requests

json = {
    "name": {name}
}

requests.post("http://{host}/app/api/v1.0/subjects/", json=json)
```
`name` - название предмета. <br>

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса для всех subjects
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
`id` - id предмета. <br>
`subject` - название предмета. <br>
#### Пример запроса для одного subject
```python
import requests

requests.get("http://{host}/app/api/v1.0/subjects/<name>")
```
`<name>` - название предмета. <br>

#### Ответ
```python
{
    "id": {id},
    "subject": {subject}
}
```
`id` - id предмета. <br>
`subject` - название предмета. <br>
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://{host}/app/api/v1.0/subjects/<name>")
```
`<name>` - название предмета. <br>

#### Ответ
```python
{
    "success": True
}
```
## 1.5 Quizzes

### POST
#### Пример запроса в формате json
```python
{
    "room_id": {room_id}
}
```
`room_id` - id комнаты квиза. <br>
#### Пример запроса
```python
import requests

json = {
    "room_id": {room_id}
}
requests.post("http://{host}/app/api/v1.0/quizzes/", json=json)
```
`room_id` - id комнаты квиза. <br>
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

requests.get("http://{host}/app/api/v1.0/quizzes/<int:room_id>")
```
`<int:room_id>` - id комнаты квиза. <br>

#### Ответ
```python
{
    "id": {id}, 
    "room_id": {room_id}, 
    "start_at": {start_at}
}
```
`id` - id квиза. <br>
`room_id` - id комнаты квиза. <br>
`start_at` - дата начала квиза.  <br>
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://{host}/app/api/v1.0/quizzes/<int:room_id>")
```
`<int:room_id>` - id комнаты квиза. <br>

#### Ответ
```python
{
    "success": True
}
```
