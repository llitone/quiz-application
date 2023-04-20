import os
import logging

from flask import Flask, request, abort, jsonify, make_response
from flask_cors import CORS

from .database.app_users.authors import Author
from .database import db_session
from .database.app_users.users import AppUser
from .database.questions.subjects import Subject
from .config import LOGGING_LEVEL, LOG_PATH, FORMAT
from .database.questions.questions import Question
from .database.questions.answers import Answer
from .database.quizzes.quiz import Quiz
from .database.quizzes.quiz_questions import QuizQuestion

if not os.path.isdir(".db"):
    os.mkdir(".db")
if not os.path.isdir(".logs"):
    os.mkdir(".logs")

handler = logging.FileHandler(LOG_PATH, mode='+a')
handler.setFormatter(logging.Formatter(FORMAT))

flask_logger = logging.getLogger("flask")
flask_logger.setLevel(LOGGING_LEVEL)
flask_logger.addHandler(handler)

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)
logger.addHandler(handler)

application = Flask(__name__)
CORS(application, resource={
    r"/*": {
        "origins": "*"
    }
})

db_session.global_init(".db/database.db")


@application.route("/")
def index():
    return "hello world"


@application.route(f"/app/api/v1.0/users/", methods=["POST"])
def register_user():
    if not request.json:
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if tuple(request.json.keys()) != ("name", "age", "phone_number", "password", "points"):
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["name"], str):
        response = make_response(jsonify({"error": "name must be str"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["age"], int):
        response = make_response(jsonify({"error": "age must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["phone_number"], str):
        response = make_response(jsonify({"error": "phone_number must be str"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["password"], str):
        response = make_response(jsonify({"error": "password must be str"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["points"], int):
        response = make_response(jsonify({"error": "points must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    try:
        new_user = AppUser()
        new_user.name = request.json["name"]
        new_user.age = request.json["age"]
        new_user.phone_number = request.json["phone_number"]
        new_user.password = request.json["password"]
        new_user.points = request.json["points"]
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "new user add error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    try:
        session = db_session.create_session()
        session.add(new_user)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/subjects/", methods=["POST"])
def add_subject():
    if not request.json:
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if tuple(request.json.keys()) != ("name",):
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["name"], str):
        response = make_response(jsonify({"error": "name must be str"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        subject = Subject()
        subject.subject = request.json["name"]
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "new session add error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        session = db_session.create_session()
        session.add(subject)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/subjects/", methods=["GET"])
def all_subjects():
    result = []

    try:
        session = db_session.create_session()
        for subject in session.query(Subject):
            result.append({"id": subject.id, "subject": subject.subject})
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify(result), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/subjects/<name>", methods=["GET", "DELETE"])
def subjects(name):
    session = db_session.create_session()
    subject = session.query(Subject).filter(Subject.subject == name).first()
    if not subject:
        abort(404)
    if request.method == "GET":
        response = make_response(jsonify({"id": subject.id, "subject": subject.subject}), 201)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        try:
            session.delete(subject)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            response = make_response(jsonify({"error": "db error"}), 500)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/questions/", methods=["POST"])
def add_question():
    if not request.json:
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if tuple(request.json.keys()) != (
            "age", "question", "difficulty", "value",
            "subject_id", "explanation", "author_id"
    ):
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["age"], int):
        response = make_response(jsonify({"error": "name must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["question"], str):
        response = make_response(jsonify({"error": "question must be str"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["difficulty"], int):
        response = make_response(jsonify({"error": "difficulty must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["value"], int):
        response = make_response(jsonify({"error": "value must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["subject_id"], int):
        response = make_response(jsonify({"error": "subject_id must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["explanation"], str):
        response = make_response(jsonify({"error": "explanation must be str"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["author_id"], int):
        response = make_response(jsonify({"error": "author_id must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        question = Question()
        question.age = request.json["age"]
        question.question = request.json["question"]
        question.difficulty = request.json["difficulty"]
        question.value = request.json["value"]
        question.subject_id = request.json["subject_id"]
        question.explanation = request.json["explanation"]
        question.author_id = request.json["author_id"]

    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "new session add error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        session = db_session.create_session()
        session.add(question)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route("/app/api/v1.0/questions/subject=<int:subject_id>")
def questions_by_subjects(subject_id):
    session = db_session.create_session()
    try:
        subject = session.query(Subject).filter(Subject.id == subject_id).first()
    except Exception as ex:
        logger.error(ex)
        abort(404)
        return
    result = []
    try:
        for question in session.query(Question).filter(Question.subject == subject):
            question_result = question.json()
            question_result["answers"] = []
            for question_answer in session.query(Answer).filter(Answer.question == question):
                question_result["answers"].append(question_answer.json())
            result.append(question_result)
    except Exception as ex:
        logger.error(ex)
        abort(500)
        return
    response = make_response(jsonify(result), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/questions/", methods=["GET"])
def all_questions():
    try:
        result = {}
        session = db_session.create_session()
        for subject in session.query(Subject):
            result[subject.subject] = []
            for question in session.query(Question).filter(Question.subject == subject):
                question_result = question.json()
                question_result["answers"] = []
                for question_answer in session.query(Answer).filter(Answer.question == question):
                    question_result["answers"].append(question_answer.json())
                result[subject.subject].append(question_result)

    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify(result), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/questions/<int:question_id>", methods=["GET", "DELETE"])
def questions(question_id):
    session = db_session.create_session()
    question = session.query(Question).filter(Question.id == question_id).first()
    if not question:
        abort(404)
    if request.method == "GET":
        response = make_response(jsonify(question.json()), 201)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        try:
            session.delete(question)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            response = make_response(jsonify({"error": "db error"}), 500)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/quizzes/", methods=["POST"])
def add_quiz():
    if not request.json:
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if tuple(request.json.keys()) != ("room_id",):
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["room_id"], int):
        response = make_response(jsonify({"error": "room_id must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        quiz = Quiz()
        quiz.room_id = request.json["room_id"]
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "new session add error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        session = db_session.create_session()
        session.add(quiz)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/quizzes/<int:room_id>", methods=["GET", "DELETE"])
def quizzes(room_id):
    session = db_session.create_session()
    quiz = session.query(Quiz).filter(Quiz.room_id == room_id).first()
    if not quiz:
        abort(404)
    if request.method == "GET":
        response = make_response(jsonify({"id": quiz.id, "room_id": quiz.room_id, "start_at": quiz.start_at}), 201)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        try:
            session.delete(quiz)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            response = make_response(jsonify({"error": "db error"}), 500)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/users/<phone>", methods=["GET"])
def get_user(phone):
    session = db_session.create_session()
    user = session.query(AppUser).filter(AppUser.phone_number == phone).first()
    if not user:
        abort(404)
        return
    response = make_response(jsonify(user.json()), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/answers/", methods=["POST"])
def add_answer():
    if not request.json:
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if tuple(request.json.keys()) != ("question_id", "answer", "is_correct"):
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["question_id"], int):
        response = make_response(jsonify({"error": "question_id must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["answer"], str):
        response = make_response(jsonify({"error": "answer must be str"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["is_correct"], bool):
        response = make_response(jsonify({"error": "is_correct must be bool"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        question_answer = Answer()
        question_answer.question_id = request.json["question_id"]
        question_answer.answer = request.json["answer"]
        question_answer.is_correct = request.json["is_correct"]
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "new session add error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        session = db_session.create_session()
        session.add(question_answer)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/answers/<int:question_id>", methods=["GET", "DELETE"])
def answer(question_id):
    session = db_session.create_session()
    question_answer = session.query(Answer).filter(Answer.question_id == question_id).first()
    if not question_answer:
        abort(404)
    if request.method == "GET":
        response = make_response(jsonify(question_answer.json()), 201)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        try:
            session.delete(question_answer)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            response = make_response(jsonify({"error": "db error"}), 500)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/quiz_questions/", methods=["POST"])
def add_quiz_questions():
    if not request.json:
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if tuple(request.json.keys()) != ("question_id", "quiz_id", "is_correct"):
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["question_id"], int):
        response = make_response(jsonify({"error": "question_id must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["quiz_id"], int):
        response = make_response(jsonify({"error": "answer must be quiz_id"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["is_correct"], bool):
        response = make_response(jsonify({"error": "is_correct must be bool"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        question_question = QuizQuestion()
        question_question.question_id = request.json["question_id"]
        question_question.quiz_id = request.json["quiz_id"]
        question_question.is_correct = request.json["is_correct"]
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "new session add error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        session = db_session.create_session()
        session.add(question_question)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/quiz_questions/<int:question_id>", methods=["GET", "DELETE"])
def quiz_question(question_id):
    session = db_session.create_session()
    question_answer = session.query(Answer).filter(Answer.question_id == question_id).first()
    if not question_answer:
        abort(404)
    if request.method == "GET":
        response = make_response(jsonify(question_answer.json()), 201)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        try:
            session.delete(question_answer)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            response = make_response(jsonify({"error": "db error"}), 500)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/authors/", methods=["POST"])
def register_author():
    if not request.json:
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if tuple(request.json.keys()) != ("login", "password"):
        response = make_response(jsonify({"error": "keys not success"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["login"], str):
        response = make_response(jsonify({"error": "name must be str"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not isinstance(request.json["password"], str):
        response = make_response(jsonify({"error": "password must be int"}), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    try:
        new_author = Author()
        new_author.login = request.json["login"]
        new_author.password = request.json["password"]

    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "new user add error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    try:
        session = db_session.create_session()
        session.add(new_author)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        response = make_response(jsonify({"error": "db error"}), 500)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route(f"/app/api/v1.0/authors/<login>", methods=["GET", "DELETE"])
def get_author(login):
    session = db_session.create_session()
    author = session.query(Author).filter(Author.login == login).first()
    if request.method == "GET":
        if not author:
            abort(404)
            return
        response = make_response(jsonify(author.json()), 201)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        try:
            session.delete(author)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            response = make_response(jsonify({"error": "db error"}), 500)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    response = make_response(jsonify({"success": True}), 201)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.errorhandler(404)
def not_found(error):
    logger.error(error)
    response = make_response(jsonify({'error': 'Not found'}), 404)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
