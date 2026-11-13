from flask import Blueprint, jsonify, request, session

from backend.service.auth_service import AuthService

bp = Blueprint("auth", __name__)


@bp.post("/api/login")
def login():
    data = request.get_json(silent=True) or request.form
    user = AuthService.login(
        data.get("identifier") or data.get("username"),
        data.get("password"),
        data.get("role") or None
    )
    session.clear()
    session["user"] = user
    return jsonify({"message": "Login successful.", "user": user})


@bp.post("/api/register")
def register():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Registration details are required."}), 400

    result = AuthService.register_student(data)
    return jsonify({
        "message": "Your student account has been created. You can now sign in.",
        "candidate_code": result["candidate_code"]
    }), 201


@bp.post("/api/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully."})
