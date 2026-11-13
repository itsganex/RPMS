from backend.dao.base_dao import BaseDAO
class InterviewDAO(BaseDAO):
    table="interview_rounds"
    primary_key="interview_id"
    allowed_columns=set(['application_id', 'round_number', 'round_type', 'interview_date', 'interview_time', 'mode', 'interviewer_name', 'interview_status'])
