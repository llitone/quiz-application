import os

from flask import Flask, request, abort, jsonify
from database import db_session
from database.app_users.users import AppUser

application = Flask(__name__)

if not os.path.isdir(".db"):
    os.mkdir(".db")

db_session.global_init(".db/database.db")


@application.route("/")
def index():
    return "hello world"


@application.route(f"/app/api/v1.0/users/", methods=["POST"])
def register_user():
    if not request.json:
        abort(400)
    print(tuple(request.json.keys()))
    if tuple(request.json.keys()) != ("name", "age", "phone_number", "password", "points"):
        return jsonify({"success": False, "error": "keys not success"}), 400
    if not isinstance(request.json["name"], str):
        return jsonify({"success": False, "error": "name must be str"}), 400
    if not isinstance(request.json["age"], int):
        return jsonify({"success": False, "error": "age must be int"}), 400
    if not isinstance(request.json["phone_number"], str):
        return jsonify({"success": False, "error": "phone_number must be str"}), 400
    if not isinstance(request.json["password"], str):
        return jsonify({"success": False, "error": "password must be str"}), 400
    if not isinstance(request.json["points"], int):
        return jsonify({"success": False, "error": "points must be int"}), 400

    try:
        new_user = AppUser()
        new_user.name = request.json["name"]
        new_user.age = request.json["age"]
        new_user.phone_number = request.json["phone_number"]
        new_user.password = request.json["password"]
        new_user.points = request.json["points"]
    except Exception as ex:
        print(ex)
        return jsonify({"success": False, "error": "user create error"}), 500

    try:
        session = db_session.create_session()
        session.add(new_user)
        session.commit()
    except Exception as ex:
        print(ex)
        return jsonify({"success": False, "error": "db error"}), 500

    return jsonify({"success": True}), 201


@application.route(f"/app/api/v1.0/users/<phone>", methods=["GET"])
def get_user(phone):
    session = db_session.create_session()
    return jsonify(session.query(AppUser).filter(AppUser.phone_number == phone).first().json())


if __name__ == "__main__":
    application.run(debug=True, port=1238)
