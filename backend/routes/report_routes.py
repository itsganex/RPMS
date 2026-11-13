from flask import Blueprint,jsonify
from backend.service.report_service import ReportService
bp=Blueprint("reports",__name__)
@bp.get("/api/reports/dashboard")
def dashboard(): return jsonify(ReportService.dashboard())
@bp.get("/api/reports/funnel")
def funnel(): return jsonify(ReportService.funnel())
@bp.get("/api/reports/pending-interviews")
def pending(): return jsonify(ReportService.pending_interviews())
@bp.get("/api/reports/company-placements")
def company_placements(): return jsonify(ReportService.company_placements())
