from backend.dao.base_dao import BaseDAO
class ApplicationDAO(BaseDAO):
    table="applications"
    primary_key="application_id"
    allowed_columns=set(['application_code', 'candidate_id', 'job_id', 'eligibility_status', 'eligibility_reason', 'application_status', 'applied_at', 'assigned_recruiter_id'])
