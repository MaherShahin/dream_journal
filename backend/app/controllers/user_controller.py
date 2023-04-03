from flask import Blueprint, request, jsonify, make_response
from backend.app.models.user import User
from backend.app.utils.security import pwd_context, create_access_token

bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route("/register", methods=["POST"])
def register():
    if not request.is_json:
        return make_response(jsonify({"message": "Missing JSON in request"}), 400)

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if not email or not password:
        return make_response(jsonify({"message": "Missing email or password"}), 400)

    existing_user = User.get_user_by_email(email)

    if existing_user:
        return make_response(jsonify({"message": "Email already registered"}), 400)

    hashed_password = pwd_context.hash(password)
    user_data = {"email": email, "hashed_password": hashed_password}
    user_id = User.create_user(user_data)
    new_user = User.get_user_by_id(user_id.inserted_id)

    return jsonify(User(new_user).to_dict()), 201

@bp.route("/users", methods=["GET"])
def get_users():
    users = User.get_all_users()
    return jsonify([User(user).to_dict() for user in users]), 200

# Add more user-related routes as needed (e.g., update, delete, login, etc.)
