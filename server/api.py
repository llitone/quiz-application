import os
import logging

from flask import Flask, request, abort, jsonify, make_response
from database import db_session
from database.app_users.users import AppUser
from server.config import LOGGING_LEVEL, LOG_PATH, FORMAT

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


@application.route(f"/app/api/v1.0/users/<phone>", methods=["GET"])
def get_user(phone):
    session = db_session.create_session()
    user = session.query(AppUser).filter(AppUser.phone_number == phone).first()
    if not user:
        abort(404)
        return
    return make_response(jsonify(user.json()), 201)


@application.errorhandler(404)
def not_found(error):
    logger.error(error)
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    application.run(debug=True, port=1238)
