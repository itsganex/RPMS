from flask import Blueprint,request,jsonify
from backend.dao.company_dao import CompanyDAO
from backend.service.company_service import CompanyService
bp=Blueprint("companies",__name__)
@bp.get("/api/companies")
def listing(): return jsonify(CompanyDAO().list())
@bp.post("/api/companies")
def create(): return jsonify({"id":CompanyService.create(request.get_json() or {})}),201
@bp.put("/api/companies/<int:rid>")
def update(rid): return jsonify({"updated":CompanyDAO().update(rid,request.get_json() or {})})
