from flask import jsonify, make_response

def create_response(message: str, status_code: int):
    return make_response(jsonify({"message": message}), status_code)
