from flask import Blueprint, request, jsonify, make_response
from backend.app.models.entry import DreamEntry
from backend.app.models.user import User

bp = Blueprint("entry", __name__, url_prefix="/entry")

@bp.route("/", methods=["POST"])
def create_entry():
    user_id = request.json.get("user_id")
    title = request.json.get("title")
    content = request.json.get("content")
    date = request.json.get("date")

    entry_data = {
        "user_id": user_id,
        "title": title,
        "content": content,
        "date": date,
    }

    entry_id = DreamEntry.create_entry(entry_data)
    new_entry = DreamEntry.get_entry_by_id(entry_id.inserted_id)

    return jsonify(new_entry.to_dict()), 201

@bp.route("/<entry_id>", methods=["PUT"])
def update_entry(entry_id):
    title = request.json.get("title")
    content = request.json.get("content")
    date = request.json.get("date")

    entry_data = {
        "title": title,
        "content": content,
        "date": date,
    }

    DreamEntry.update_entry(entry_id, entry_data)
    updated_entry = DreamEntry.get_entry_by_id(entry_id)

    return jsonify(updated_entry.to_dict()), 200

@bp.route("/<entry_id>", methods=["DELETE"])
def delete_entry(entry_id):
    result = DreamEntry.delete_entry(entry_id)
    if result.deleted_count == 1:
        return make_response(jsonify({"message": "Entry deleted"}), 200)
    else:
        return make_response(jsonify({"message": "Entry not found"}), 404)

@bp.route("/user/<user_id>", methods=["GET"])
def get_entries(user_id):
    entries = DreamEntry.get_entries_by_user_id(user_id)
    return jsonify([entry.to_dict() for entry in entries]), 200

# Add more entry-related routes as needed
