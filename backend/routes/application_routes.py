from flask import Blueprint,request,jsonify,session
from backend.database import Database
from backend.service.application_service import ApplicationService
bp=Blueprint("applications",__name__)
@bp.get("/api/applications")
def listing():
    return jsonify(Database.fetch_all("""SELECT a.*,c.full_name,j.job_title,co.company_name FROM applications a
      JOIN candidates c ON c.candidate_id=a.candidate_id JOIN jobs j ON j.job_id=a.job_id
      JOIN companies co ON co.company_id=j.company_id ORDER BY a.application_id DESC"""))
@bp.post("/api/applications/check")
def check():
    from backend.service.eligibility_service import EligibilityService
    d=request.get_json() or {}
    return jsonify(EligibilityService.check(int(d["candidate_id"]),int(d["job_id"])))
@bp.post("/api/applications")
def apply():
    d=request.get_json() or {}
    return jsonify({"id":ApplicationService.apply(int(d["candidate_id"]),int(d["job_id"]),session.get("user",{}).get("user_id"))}),201
@bp.post("/api/applications/<int:rid>/status")
def status(rid):
    d=request.get_json() or {}
    ApplicationService.change_status(rid,d["status"],d.get("remarks",""),session.get("user",{}).get("user_id"))
    return jsonify({"message":"Application status updated"})
@bp.get("/api/applications/<int:rid>/history")
def history(rid):
    return jsonify(Database.fetch_all("SELECT * FROM application_history WHERE application_id=%s ORDER BY changed_at",(rid,)))
