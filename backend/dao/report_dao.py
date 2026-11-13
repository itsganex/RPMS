from backend.database import Database
class ReportDAO:
    @staticmethod
    def dashboard():
        sql = '''
        SELECT
          (SELECT COUNT(*) FROM candidates) total_candidates,
          (SELECT COUNT(*) FROM candidates WHERE profile_status='ACTIVE') active_candidates,
          (SELECT COUNT(*) FROM companies WHERE status='ACTIVE') companies,
          (SELECT COUNT(*) FROM jobs WHERE job_status='OPEN') open_jobs,
          (SELECT COUNT(*) FROM applications) applications,
          (SELECT COUNT(*) FROM interview_rounds) interviews,
          (SELECT COUNT(*) FROM applications WHERE application_status='SELECTED') selected,
          (SELECT COUNT(*) FROM placements WHERE joining_status='JOINED') placed
        '''
        return Database.fetch_one(sql)
    @staticmethod
    def recruitment_funnel():
        return Database.fetch_all("SELECT application_status label, COUNT(*) value FROM applications GROUP BY application_status ORDER BY value DESC")
    @staticmethod
    def pending_interviews():
        return Database.fetch_all("""SELECT i.*, a.application_code, c.full_name, j.job_title, co.company_name
          FROM interview_rounds i JOIN applications a ON a.application_id=i.application_id
          JOIN candidates c ON c.candidate_id=a.candidate_id JOIN jobs j ON j.job_id=a.job_id
          JOIN companies co ON co.company_id=j.company_id
          WHERE i.interview_status IN ('SCHEDULED','RESCHEDULED') ORDER BY i.interview_date LIMIT 20""")
    @staticmethod
    def company_placements():
        return Database.fetch_all("""SELECT co.company_name, COUNT(p.placement_id) placed_count
          FROM companies co LEFT JOIN placements p ON p.company_id=co.company_id AND p.joining_status='JOINED'
          GROUP BY co.company_id, co.company_name ORDER BY placed_count DESC""")
