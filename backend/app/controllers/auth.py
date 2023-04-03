# Add imports at the top
from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token
from flask import Blueprint
from backend.app.models.user import User
from backend.app.utils.security import security

bp = Blueprint("auth", __name__, url_prefix="/auth")

# User registration
@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return make_response(jsonify({"message": "Missing JSON in request"}), 400)

    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return make_response(jsonify({"message": "Missing email or password"}), 400)

    user = User.get_by_email(email)
    if user:
        return make_response(jsonify({"message": "Email already registered"}), 400)

    hashed_password = security.generate_password_hash(password)
    user = User(email=email, hashed_password=hashed_password)
    user.save()

    return make_response(jsonify(user.to_dict()), 201)

# User login
@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return make_response(jsonify({"message": "Missing JSON in request"}), 400)

    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return make_response(jsonify({"message": "Missing email or password"}), 400)

    user = User.get_by_email(email)
    if not user or not security.check_password_hash(user.hashed_password, password):
        return make_response(jsonify({"message": "Invalid email or password"}), 401)

    access_token = create_access_token(identity=user.id)
    return make_response(jsonify({"access_token": access_token}), 200)

# User logout
@bp.route("/logout", methods=["POST"])
def logout():
    # With JWT, there's no need for a specific logout function. The client can simply remove the JWT token.
    return make_response(jsonify({"message": "Logout successful"}), 200)
