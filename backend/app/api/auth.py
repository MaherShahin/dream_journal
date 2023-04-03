from flask import Blueprint, request, jsonify
from backend.app.utils import security
from backend.app.models.user import User
from backend.app.models.entry import DreamEntry
from backend.app.utils.database import mongo

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["POST"])
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if not email or not password:
        return jsonify({"msg": "Missing email or password"}), 400

    users = mongo.db.users
    user = users.find_one({"email": email})

    if user:
        return jsonify({"msg": "Email already registered"}), 400

    hashed_password = security.pwd_context.hash(password)
    user = {"email": email, "hashed_password": hashed_password}
    users.insert_one(user)

    return jsonify(User(user)), 201

@bp.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    return jsonify([User(user) for user in users]), 200
