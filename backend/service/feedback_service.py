from backend.database import Database
class FeedbackService:
    @staticmethod
    def save(interview_id,data,user_id=None):
        def work(conn,cur):
            cur.execute("""SELECT i.application_id,i.interview_status,a.application_status
                FROM interview_rounds i JOIN applications a ON a.application_id=i.application_id
                WHERE i.interview_id=%s FOR UPDATE""",(interview_id,))
            row=cur.fetchone()
            if not row: raise ValueError("Interview not found.")
            cur.execute("""INSERT INTO interview_feedback(interview_id,technical_rating,communication_rating,problem_solving_rating,overall_rating,feedback_remarks,recommendation)
                VALUES(%s,%s,%s,%s,%s,%s,%s)""",(interview_id,data.get("technical_rating"),data.get("communication_rating"),data.get("problem_solving_rating"),data.get("overall_rating"),data.get("feedback_remarks"),data.get("recommendation")))
            cur.execute("UPDATE interview_rounds SET interview_status='COMPLETED' WHERE interview_id=%s",(interview_id,))
            result=data.get("recommendation")
            old=row["application_status"]
            if result in ("SELECTED","REJECTED") and old in ("INTERVIEW_SCHEDULED","INTERVIEWED","SHORTLISTED"):
                new=result
            elif result=="NEXT_ROUND":
                new="INTERVIEWED"
            else:
                new=old
            if new!=old:
                cur.execute("UPDATE applications SET application_status=%s WHERE application_id=%s",(new,row["application_id"]))
                cur.execute("INSERT INTO application_history(application_id,old_status,new_status,remarks,changed_by) VALUES(%s,%s,%s,'Interview feedback submitted',%s)",(row["application_id"],old,new,user_id))
        Database.transaction(work)
