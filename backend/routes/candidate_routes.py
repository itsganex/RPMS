from flask import Blueprint,request,jsonify,session
from backend.dao.candidate_dao import CandidateDAO
from backend.service.candidate_service import CandidateService
from backend.database import Database
bp=Blueprint("candidates",__name__)
@bp.get("/api/candidates")
def listing():
    q=request.args.get("q","")
    return jsonify(CandidateDAO().list("full_name LIKE %s OR email LIKE %s",(f"%{q}%",f"%{q}%")) if q else CandidateDAO().list())
@bp.get("/api/candidates/<int:rid>")
def detail(rid):
    row=CandidateDAO().get(rid)
    return (jsonify(row),200) if row else (jsonify({"error":"Candidate not found"}),404)
@bp.post("/api/candidates")
def create():
    return jsonify({"id":CandidateService.create(request.get_json() or {},session.get("user",{}).get("user_id"))}),201
@bp.put("/api/candidates/<int:rid>")
def update(rid):
    return jsonify({"updated":CandidateService.update(rid,request.get_json() or {})})
@bp.post("/api/candidates/<int:rid>/deactivate")
def deactivate(rid):
    Database.execute("UPDATE candidates SET profile_status='INACTIVE' WHERE candidate_id=%s",(rid,))
    return jsonify({"message":"Candidate deactivated"})
