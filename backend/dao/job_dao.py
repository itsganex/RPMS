from backend.dao.base_dao import BaseDAO
class JobDAO(BaseDAO):
    table="jobs"
    primary_key="job_id"
    allowed_columns=set(['company_id', 'job_code', 'job_title', 'openings', 'employment_type', 'location', 'min_package', 'max_package', 'qualification', 'min_percentage', 'min_passing_year', 'max_passing_year', 'max_backlogs', 'experience_required', 'required_technology', 'posted_date', 'application_deadline', 'job_status', 'created_by'])
