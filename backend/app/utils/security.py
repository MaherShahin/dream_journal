from passlib.context import CryptContext
from flask_jwt_extended import JWTManager

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
jwt = JWTManager()
