from backend.dao.job_dao import JobDAO
from backend.util.validators import required, percentage, non_negative
from backend.exception.custom_exceptions import ValidationError
class JobService:
    dao=JobDAO()
    @classmethod
    def create(cls,data):
        required(data,"company_id","job_code","job_title","openings","posted_date","application_deadline")
        if int(data["openings"])<=0: raise ValidationError("Openings must be greater than zero.")
        if float(data.get("min_package") or 0)>float(data.get("max_package") or 0): raise ValidationError("Minimum package cannot exceed maximum package.")
        percentage(data.get("min_percentage")); non_negative(data.get("max_backlogs",0),"Maximum backlogs")
        if data["application_deadline"] < data["posted_date"]: raise ValidationError("Deadline cannot be before posted date.")
        return cls.dao.create(data)
