from pathlib import Path

from flask import Flask, jsonify, redirect, request, send_from_directory, session
from werkzeug.exceptions import HTTPException

from backend.config import Config
from backend.exception.custom_exceptions import RPMSException
from backend.routes.auth_routes import bp as auth_bp
from backend.routes.candidate_routes import bp as candidate_bp
from backend.routes.company_routes import bp as company_bp
from backend.routes.job_routes import bp as job_bp
from backend.routes.application_routes import bp as application_bp
from backend.routes.interview_routes import bp as interview_bp
from backend.routes.placement_routes import bp as placement_bp
from backend.routes.report_routes import bp as report_bp
from backend.routes.student_routes import bp as student_bp

FRONTEND = Path(__file__).resolve().parents[1] / "frontend"
STAFF_ROLES = {"ADMIN", "RECRUITER", "PLACEMENT_OFFICER"}
MANAGEMENT_ROLES = {"ADMIN", "PLACEMENT_OFFICER"}


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)

    for blueprint in (
        auth_bp, candidate_bp, company_bp, job_bp,
        application_bp, interview_bp, placement_bp, report_bp, student_bp
    ):
        app.register_blueprint(blueprint)

    @app.before_request
    def protect_routes():
        path = request.path

        public_paths = {
            "/", "/login.html", "/register.html",
            "/api/login", "/api/register", "/api/logout"
        }
        public_assets = path.startswith(("/css/", "/js/", "/images/"))

        if path in public_paths or public_assets:
            return None

        user = session.get("user")
        if not user:
            if path.startswith("/api/"):
                return jsonify({"error": "Please sign in first."}), 401
            if path.endswith(".html"):
                return redirect("/login.html")
            return None

        role = user.get("role")

        if path.startswith("/api/student/") or path == "/student-dashboard.html":
            if role != "STUDENT":
                if path.startswith("/api/"):
                    return jsonify({"error": "This page is only available to student accounts."}), 403
                return redirect("/dashboard.html")
            return None

        if role == "STUDENT":
            if path.startswith("/api/"):
                return jsonify({"error": "Student accounts cannot access staff operations."}), 403
            if path.endswith(".html") and path != "/student-dashboard.html":
                return redirect("/student-dashboard.html")

        if path.startswith("/api/"):
            if path.startswith(("/api/companies", "/api/jobs", "/api/candidates",
                                "/api/applications", "/api/interviews")) and role not in STAFF_ROLES:
                return jsonify({"error": "Your role cannot access recruitment operations."}), 403
            if path.startswith(("/api/offers", "/api/placements")) and role not in MANAGEMENT_ROLES:
                return jsonify({"error": "Only administrators or placement officers can manage offers and placements."}), 403
            if path.startswith("/api/reports") and role not in STAFF_ROLES:
                return jsonify({"error": "Your role cannot access reports."}), 403

        return None

    @app.get("/")
    def home():
        user = session.get("user")
        if user:
            return redirect("/student-dashboard.html" if user.get("role") == "STUDENT" else "/dashboard.html")
        return send_from_directory(FRONTEND, "login.html")

    @app.get("/<path:filename>")
    def frontend(filename):
        return send_from_directory(FRONTEND, filename)

    @app.errorhandler(RPMSException)
    def business_error(exc):
        return jsonify({"error": str(exc)}), 400

    @app.errorhandler(ValueError)
    def validation_error(exc):
        return jsonify({"error": str(exc)}), 400

    @app.errorhandler(Exception)
    def unexpected_error(exc):
        if isinstance(exc, HTTPException):
            return exc
        app.logger.exception("Unhandled application error")
        message = str(exc) if app.debug else "An unexpected error occurred."
        return jsonify({"error": message}), 500

    return app
