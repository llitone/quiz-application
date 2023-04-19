import os
import logging

from flask import Flask, request, abort, jsonify, make_response

from database import db_session
from database.app_users.users import AppUser
from database.questions.subjects import Subject
from server.config import LOGGING_LEVEL, LOG_PATH, FORMAT
from server.database.questions.questions import Question
from server.database.questions.answers import Answer
from server.database.quizzes.quiz import Quiz

if not os.path.isdir(".db"):
    os.mkdir(".db")
if not os.path.isdir(".logs"):
    os.mkdir(".logs")

handler = logging.FileHandler(LOG_PATH, mode='+a')
handler.setFormatter(logging.Formatter(FORMAT))

flask_logger = logging.getLogger("flask")
flask_logger.addHandler(handler)

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)
logger.addHandler(handler)

application = Flask(__name__)

db_session.global_init(".db/database.db")


@application.route("/")
def index():
    return "hello world"


@application.route(f"/app/api/v1.0/users/", methods=["POST"])
def register_user():
    if not request.json:
        return make_response(jsonify({"error": "keys not success"}), 400)
    if tuple(request.json.keys()) != ("name", "age", "phone_number", "password", "points"):
        return make_response(jsonify({"error": "keys not success"}), 400)
    if not isinstance(request.json["name"], str):
        return make_response(jsonify({"error": "name must be str"}), 400)
    if not isinstance(request.json["age"], int):
        return make_response(jsonify({"error": "age must be int"}), 400)
    if not isinstance(request.json["phone_number"], str):
        return make_response(jsonify({"error": "phone_number must be str"}), 400)
    if not isinstance(request.json["password"], str):
        return make_response(jsonify({"error": "password must be str"}), 400)
    if not isinstance(request.json["points"], int):
        return make_response(jsonify({"error": "points must be int"}), 400)

    try:
        new_user = AppUser()
        new_user.name = request.json["name"]
        new_user.age = request.json["age"]
        new_user.phone_number = request.json["phone_number"]
        new_user.password = request.json["password"]
        new_user.points = request.json["points"]
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "new user add error"}), 500)

    try:
        session = db_session.create_session()
        session.add(new_user)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "db error"}), 500)

    return make_response(jsonify({"success": True}), 201)


@application.route(f"/app/api/v1.0/subjects/", methods=["POST"])
def add_subject():
    if not request.json:
        return make_response(jsonify({"error": "keys not success"}), 400)
    if tuple(request.json.keys()) != ("name",):
        return make_response(jsonify({"error": "keys not success"}), 400)
    if not isinstance(request.json["name"], str):
        return make_response(jsonify({"error": "name must be str"}), 400)
    try:
        subject = Subject()
        subject.subject = request.json["name"]
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "new session add error"}), 500)
    try:
        session = db_session.create_session()
        session.add(subject)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "db error"}), 500)
    return make_response(jsonify({"success": True}), 201)


@application.route(f"/app/api/v1.0/subjects/<name>", methods=["GET", "DELETE"])
def subjects(name):
    session = db_session.create_session()
    subject = session.query(Subject).filter(Subject.subject == name).first()
    if not subject:
        abort(404)
    if request.method == "GET":
        return {"id": subject.id, "subject": subject.subject}
    else:
        try:
            session.delete(subject)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            return make_response(jsonify({"error": "db error"}), 500)


@application.route(f"/app/api/v1.0/questions/", methods=["POST"])
def add_question():
    if not request.json:
        return make_response(jsonify({"error": "keys not success"}), 400)
    if tuple(request.json.keys()) != ("age", "question", "difficulty", "value", "subject_id", "explanation"):
        return make_response(jsonify({"error": "keys not success"}), 400)
    if not isinstance(request.json["age"], int):
        return make_response(jsonify({"error": "name must be int"}), 400)
    if not isinstance(request.json["question"], str):
        return make_response(jsonify({"error": "question must be str"}), 400)
    if not isinstance(request.json["difficulty"], int):
        return make_response(jsonify({"error": "difficulty must be int"}), 400)
    if not isinstance(request.json["value"], int):
        return make_response(jsonify({"error": "value must be int"}), 400)
    if not isinstance(request.json["subject_id"], int):
        return make_response(jsonify({"error": "subject_id must be int"}), 400)
    if not isinstance(request.json["explanation"], str):
        return make_response(jsonify({"error": "explanation must be str"}), 400)
    try:
        question = Question()
        question.age = request.json["age"]
        question.question = request.json["question"]
        question.difficulty = request.json["difficulty"]
        question.value = request.json["value"]
        question.subject_id = request.json["subject_id"]
        question.explanation = request.json["explanation"]
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "new session add error"}), 500)
    try:
        session = db_session.create_session()
        session.add(question)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "db error"}), 500)
    return make_response(jsonify({"success": True}), 201)


@application.route(f"/app/api/v1.0/questions/<int:question_id>", methods=["GET", "DELETE"])
def questions(question_id):
    session = db_session.create_session()
    question = session.query(Question).filter(Question.id == question_id).first()
    if not question:
        abort(404)
    if request.method == "GET":
        return make_response(jsonify(question.json()), 201)
    else:
        try:
            session.delete(question)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            return make_response(jsonify({"error": "db error"}), 500)


@application.route(f"/app/api/v1.0/quizzes/", methods=["POST"])
def add_quiz():
    if not request.json:
        return make_response(jsonify({"error": "keys not success"}), 400)
    if tuple(request.json.keys()) != ("room_id",):
        return make_response(jsonify({"error": "keys not success"}), 400)
    if not isinstance(request.json["room_id"], int):
        return make_response(jsonify({"error": "room_id must be int"}), 400)
    try:
        quiz = Quiz()
        quiz.room_id = request.json["room_id"]
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "new session add error"}), 500)
    try:
        session = db_session.create_session()
        session.add(quiz)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "db error"}), 500)
    return make_response(jsonify({"success": True}), 201)


@application.route(f"/app/api/v1.0/quizzes/<int:room_id>", methods=["GET", "DELETE"])
def quizzes(room_id):
    session = db_session.create_session()
    quiz = session.query(Quiz).filter(Quiz.room_id == room_id).first()
    if not quiz:
        abort(404)
    if request.method == "GET":
        return {"id": quiz.id, "room_id": quiz.room_id, "start_at": quiz.start_at}
    else:
        try:
            session.delete(quiz)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            return make_response(jsonify({"error": "db error"}), 500)


@application.route(f"/app/api/v1.0/users/<phone>", methods=["GET"])
def get_user(phone):
    session = db_session.create_session()
    user = session.query(AppUser).filter(AppUser.phone_number == phone).first()
    if not user:
        abort(404)
        return
    return make_response(jsonify(user.json()), 201)


@application.route(f"/app/api/v1.0/answer/", methods=["POST"])
def add_answer():
    if not request.json:
        return make_response(jsonify({"error": "keys not success"}), 400)
    if tuple(request.json.keys()) != ("question_id", "answer", "is_correct"):
        return make_response(jsonify({"error": "keys not success"}), 400)
    if not isinstance(request.json["question_id"], int):
        return make_response(jsonify({"error": "question_id must be int"}), 400)
    if not isinstance(request.json["answer"], str):
        return make_response(jsonify({"error": "answer must be str"}), 400)
    if not isinstance(request.json["is_correct"], bool):
        return make_response(jsonify({"error": "is_correct must be bool"}), 400)
    try:
        question_answer = Answer()
        question_answer.question_id = request.json["question_id"]
        question_answer.answer = request.json["answer"]
        question_answer.is_correct = request.json["is_correct"]
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "new session add error"}), 500)
    try:
        session = db_session.create_session()
        session.add(answer)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        return make_response(jsonify({"error": "db error"}), 500)
    return make_response(jsonify({"success": True}), 201)


@application.route(f"/app/api/v1.0/answer/<int:question_id>", methods=["GET", "DELETE"])
def answer(question_id):
    session = db_session.create_session()
    question_answer = session.query(Answer).filter(Answer.question_id == question_id).first()
    if not question_answer:
        abort(404)
    if request.method == "GET":
        return question_answer.json()
    else:
        try:
            session.delete(question_answer)
            session.commit()
        except Exception as ex:
            logger.error(ex)
            return make_response(jsonify({"error": "db error"}), 500)


@application.errorhandler(404)
def not_found(error):
    logger.error(error)
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    application.run(host="127.0.0.1", debug=True, port=1238)
