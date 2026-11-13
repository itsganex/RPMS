from flask import Blueprint,request,jsonify,session
from backend.dao.interview_dao import InterviewDAO
from backend.service.interview_service import InterviewService
from backend.service.feedback_service import FeedbackService
from backend.database import Database
bp=Blueprint("interviews",__name__)
@bp.get("/api/interviews")
def listing():
    return jsonify(Database.fetch_all("""SELECT i.*,a.application_code,c.full_name,j.job_title,co.company_name
      FROM interview_rounds i JOIN applications a ON a.application_id=i.application_id
      JOIN candidates c ON c.candidate_id=a.candidate_id JOIN jobs j ON j.job_id=a.job_id
      JOIN companies co ON co.company_id=j.company_id ORDER BY i.interview_date DESC"""))
@bp.post("/api/interviews")
def create(): return jsonify({"id":InterviewService.create(request.get_json() or {},session.get("user",{}).get("user_id"))}),201
@bp.put("/api/interviews/<int:rid>")
def update(rid): return jsonify({"updated":InterviewDAO().update(rid,request.get_json() or {})})
@bp.post("/api/interviews/<int:rid>/feedback")
def feedback(rid):
    FeedbackService.save(rid,request.get_json() or {},session.get("user",{}).get("user_id"))
    return jsonify({"message":"Feedback saved"})
