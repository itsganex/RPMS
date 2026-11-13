from flask import Blueprint,request,jsonify
from backend.dao.job_dao import JobDAO
from backend.service.job_service import JobService
from backend.database import Database
bp=Blueprint("jobs",__name__)
@bp.get("/api/jobs")
def listing(): return jsonify(Database.fetch_all("SELECT j.*,c.company_name FROM jobs j JOIN companies c ON c.company_id=j.company_id ORDER BY j.job_id DESC"))
@bp.post("/api/jobs")
def create(): return jsonify({"id":JobService.create(request.get_json() or {})}),201
@bp.put("/api/jobs/<int:rid>")
def update(rid): return jsonify({"updated":JobDAO().update(rid,request.get_json() or {})})
@bp.post("/api/jobs/<int:rid>/close")
def close(rid):
    Database.execute("UPDATE jobs SET job_status='CLOSED' WHERE job_id=%s",(rid,))
    return jsonify({"message":"Job closed"})
