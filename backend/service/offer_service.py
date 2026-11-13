from backend.database import Database
from backend.util.id_generator import business_code
from backend.util.logger import log_activity
class OfferService:
    @staticmethod
    def create(data,user_id=None):
        def work(conn,cur):
            cur.execute("SELECT application_status FROM applications WHERE application_id=%s FOR UPDATE",(data["application_id"],))
            row=cur.fetchone()
            if not row or row["application_status"]!="SELECTED": raise ValueError("An offer can only be created for a SELECTED application.")
            cur.execute("SELECT COALESCE(MAX(offer_id),0)+1 FROM offers"); code=business_code("OFF",cur.fetchone()[0])
            cur.execute("""INSERT INTO offers(offer_code,application_id,designation,offered_package,offer_date,expected_joining_date,offer_status)
                VALUES(%s,%s,%s,%s,%s,%s,'OFFERED')""",(code,data["application_id"],data["designation"],data["offered_package"],data["offer_date"],data.get("expected_joining_date")))
            oid=cur.lastrowid
            cur.execute("UPDATE applications SET application_status='OFFERED' WHERE application_id=%s",(data["application_id"],))
            cur.execute("INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by) VALUES(%s,'SELECTED','OFFERED','Offer created',%s)",(data["application_id"],user_id))
            return oid
        oid=Database.transaction(work); log_activity(f"Offer Created: OFF-{oid}",user_id); return oid
