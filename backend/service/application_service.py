from backend.database import Database
from backend.service.eligibility_service import EligibilityService
from backend.dao.application_dao import ApplicationDAO
from backend.exception.custom_exceptions import InvalidTransitionError, CandidateNotEligibleError
from backend.util.id_generator import business_code
from backend.util.logger import log_activity
ALLOWED={
 "APPLIED":{"ELIGIBILITY_VERIFIED","REJECTED","WITHDRAWN"},
 "ELIGIBILITY_VERIFIED":{"SHORTLISTED","REJECTED","WITHDRAWN"},
 "SHORTLISTED":{"INTERVIEW_SCHEDULED","REJECTED","WITHDRAWN"},
 "INTERVIEW_SCHEDULED":{"INTERVIEWED","REJECTED","WITHDRAWN"},
 "INTERVIEWED":{"SHORTLISTED","SELECTED","REJECTED","WITHDRAWN"},
 "SELECTED":{"OFFERED","REJECTED","WITHDRAWN"},
 "OFFERED":{"JOINED","WITHDRAWN"},
 "JOINED":set(),"REJECTED":set(),"WITHDRAWN":set()
}
class ApplicationService:
    @staticmethod
    def apply(candidate_id,job_id,user_id=None):
        eligibility=EligibilityService.check(candidate_id,job_id)
        if eligibility["eligibility_status"]!="ELIGIBLE":
            raise CandidateNotEligibleError(eligibility["eligibility_reason"])
        def work(conn,cur):
            cur.execute("SELECT COALESCE(MAX(application_id),0)+1 FROM applications")
            code=business_code("APP",cur.fetchone()[0])
            cur.execute("""INSERT INTO applications(application_code,candidate_id,job_id,eligibility_status,eligibility_reason,application_status,assigned_recruiter_id)
                VALUES(%s,%s,%s,'ELIGIBLE',%s,'APPLIED',%s)""",(code,candidate_id,job_id,eligibility["eligibility_reason"],user_id))
            aid=cur.lastrowid
            cur.execute("INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by) VALUES(%s,NULL,'APPLIED','Application submitted',%s)",(aid,user_id))
            return aid
        aid=Database.transaction(work); log_activity(f"Application Created: APP-{aid}",user_id); return aid
    @staticmethod
    def change_status(application_id,new_status,remarks="",user_id=None):
        def work(conn,cur):
            cur.execute("SELECT application_status FROM applications WHERE application_id=%s FOR UPDATE",(application_id,))
            row=cur.fetchone()
            if not row: raise ValueError("Application not found.")
            old=row["application_status"]
            if new_status not in ALLOWED.get(old,set()):
                raise InvalidTransitionError(f"Invalid application transition: {old} -> {new_status}")
            cur.execute("UPDATE applications SET application_status=%s WHERE application_id=%s",(new_status,application_id))
            cur.execute("INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by) VALUES(%s,%s,%s,%s,%s)",(application_id,old,new_status,remarks,user_id))
        Database.transaction(work); log_activity(f"Application {application_id}: {new_status}",user_id)
