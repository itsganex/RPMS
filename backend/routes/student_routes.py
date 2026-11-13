from flask import Blueprint, jsonify, request, session

from backend.database import Database
from backend.service.application_service import ApplicationService

bp = Blueprint("student", __name__)


def current_candidate_id():
    user = session.get("user") or {}
    candidate_id = user.get("candidate_id")
    if not candidate_id:
        raise ValueError("This student account is not linked to a candidate profile.")
    return int(candidate_id)


@bp.get("/api/student/profile")
def profile():
    candidate_id = current_candidate_id()
    row = Database.fetch_one(
        "SELECT * FROM candidates WHERE candidate_id = %s",
        (candidate_id,)
    )
    if not row:
        return jsonify({"error": "Student profile not found."}), 404
    return jsonify(row)


@bp.get("/api/student/jobs")
def jobs():
    rows = Database.fetch_all(
        """SELECT j.job_id, j.job_code, j.job_title, j.employment_type,
                  j.location, j.min_package, j.max_package, j.qualification,
                  j.min_percentage, j.application_deadline, j.required_technology,
                  c.company_name
           FROM jobs j
           JOIN companies c ON c.company_id = j.company_id
           WHERE j.job_status = 'OPEN'
             AND j.application_deadline >= CURDATE()
           ORDER BY j.posted_date DESC, j.job_id DESC"""
    )
    return jsonify(rows)


@bp.get("/api/student/applications")
def applications():
    candidate_id = current_candidate_id()
    rows = Database.fetch_all(
        """SELECT a.application_code, a.application_status, a.eligibility_status,
                  a.applied_at, j.job_title, j.location, co.company_name
           FROM applications a
           JOIN jobs j ON j.job_id = a.job_id
           JOIN companies co ON co.company_id = j.company_id
           WHERE a.candidate_id = %s
           ORDER BY a.applied_at DESC""",
        (candidate_id,)
    )
    return jsonify(rows)


@bp.post("/api/student/apply")
def apply():
    candidate_id = current_candidate_id()
    data = request.get_json(silent=True) or {}
    try:
        job_id = int(data.get("job_id"))
    except (TypeError, ValueError):
        return jsonify({"error": "Select a valid job."}), 400

    application_id = ApplicationService.apply(candidate_id, job_id, None)
    return jsonify({
        "message": "Your application has been submitted.",
        "application_id": application_id
    }), 201
