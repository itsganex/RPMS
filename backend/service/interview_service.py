from backend.database import Database
from backend.util.logger import log_activity
from backend.util.id_generator import business_code
class InterviewService:
    @staticmethod
    def create(data,user_id=None):
        required=["application_id","round_number","round_type","interview_date","mode"]
        if not all(data.get(k) not in (None,"") for k in required):
            raise ValueError("Application, round, date and mode are required.")
        def work(conn,cur):
            cur.execute("SELECT application_status FROM applications WHERE application_id=%s FOR UPDATE",(data["application_id"],))
            app=cur.fetchone()
            if not app: raise ValueError("Application not found.")
            if app["application_status"] not in ("SHORTLISTED","INTERVIEW_SCHEDULED","INTERVIEWED"):
                raise ValueError("Only shortlisted or active interview applications can be scheduled.")
            cur.execute("""INSERT INTO interview_rounds(application_id,round_number,round_type,interview_date,interview_time,mode,interviewer_name,interview_status)
                VALUES(%s,%s,%s,%s,%s,%s,%s,'SCHEDULED')""",(data["application_id"],data["round_number"],data["round_type"],data["interview_date"],data.get("interview_time"),data["mode"],data.get("interviewer_name")))
            iid=cur.lastrowid
            if app["application_status"]=="SHORTLISTED":
                cur.execute("UPDATE applications SET application_status='INTERVIEW_SCHEDULED' WHERE application_id=%s",(data["application_id"],))
                cur.execute("INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by) VALUES(%s,'SHORTLISTED','INTERVIEW_SCHEDULED','Interview scheduled',%s)",(data["application_id"],user_id))
            return iid
        iid=Database.transaction(work)
        log_activity(f"Interview Scheduled: INT-{iid}",user_id)
        return iid
