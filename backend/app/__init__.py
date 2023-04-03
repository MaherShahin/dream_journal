from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

from backend.app.utils import database, security
from backend.app.api import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object("backend.app.config")

    database.mongo.init_app(app)
    security.jwt.init_app(app)

    app.register_blueprint(auth.bp)

    return app
