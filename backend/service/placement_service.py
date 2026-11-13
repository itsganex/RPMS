from backend.database import Database
from backend.util.logger import log_activity
class PlacementService:
    @staticmethod
    def confirm(data,user_id=None):
        def work(conn,cur):
            cur.execute("""SELECT o.application_id,a.candidate_id,j.company_id FROM offers o
                JOIN applications a ON a.application_id=o.application_id JOIN jobs j ON j.job_id=a.job_id
                WHERE o.offer_id=%s AND o.offer_status='ACCEPTED' FOR UPDATE""",(data["offer_id"],))
            row=cur.fetchone()
            if not row: raise ValueError("A valid ACCEPTED offer is required before joining confirmation.")
            cur.execute("""INSERT INTO placements(offer_id,candidate_id,company_id,actual_joining_date,joining_status,final_package,designation)
                VALUES(%s,%s,%s,%s,'JOINED',%s,%s)""",(data["offer_id"],row["candidate_id"],row["company_id"],data["actual_joining_date"],data["final_package"],data["designation"]))
            cur.execute("UPDATE candidates SET placement_status='PLACED' WHERE candidate_id=%s",(row["candidate_id"],))
            cur.execute("UPDATE applications SET application_status='JOINED' WHERE application_id=%s",(row["application_id"],))
            cur.execute("INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by) VALUES(%s,'OFFERED','JOINED','Joining confirmed',%s)",(row["application_id"],user_id))
            return cur.lastrowid
        pid=Database.transaction(work); log_activity(f"Placement Confirmed: {pid}",user_id); return pid
