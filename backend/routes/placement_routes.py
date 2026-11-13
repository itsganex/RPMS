from flask import Blueprint,request,jsonify,session
from backend.database import Database
from backend.service.offer_service import OfferService
from backend.service.placement_service import PlacementService
bp=Blueprint("placement",__name__)
@bp.get("/api/offers")
def offers(): return jsonify(Database.fetch_all("SELECT * FROM offers ORDER BY offer_id DESC"))
@bp.post("/api/offers")
def create_offer(): return jsonify({"id":OfferService.create(request.get_json() or {},session.get("user",{}).get("user_id"))}),201
@bp.put("/api/offers/<int:rid>")
def update_offer(rid):
    d=request.get_json() or {}
    Database.execute("UPDATE offers SET offer_status=%s WHERE offer_id=%s",(d["offer_status"],rid))
    return jsonify({"message":"Offer updated"})
@bp.post("/api/placements")
def placement(): return jsonify({"id":PlacementService.confirm(request.get_json() or {},session.get("user",{}).get("user_id"))}),201
@bp.get("/api/placements")
def placements(): return jsonify(Database.fetch_all("SELECT p.*,c.full_name,co.company_name FROM placements p JOIN candidates c ON c.candidate_id=p.candidate_id JOIN companies co ON co.company_id=p.company_id ORDER BY p.placement_id DESC"))
