from datetime import date
from backend.database import Database
from backend.exception.custom_exceptions import CandidateNotFoundError, JobNotFoundError, DuplicateApplicationError
class EligibilityService:
    @staticmethod
    def check(candidate_id, job_id):
        c=Database.fetch_one("SELECT * FROM candidates WHERE candidate_id=%s",(candidate_id,))
        j=Database.fetch_one("SELECT * FROM jobs WHERE job_id=%s",(job_id,))
        if not c: raise CandidateNotFoundError("Candidate was not found.")
        if not j: raise JobNotFoundError("Job was not found.")
        reasons=[]
        if c["profile_status"]!="ACTIVE": reasons.append("Candidate profile is not ACTIVE")
        if j["job_status"]!="OPEN": reasons.append("Job is not OPEN")
        if j["application_deadline"] and j["application_deadline"] < date.today(): reasons.append("Application deadline has passed")
        if Database.fetch_one("SELECT application_id FROM applications WHERE candidate_id=%s AND job_id=%s",(candidate_id,job_id)):
            raise DuplicateApplicationError("Candidate has already applied for this job.")
        if j["min_percentage"] and (c["percentage"] is None or float(c["percentage"]) < float(j["min_percentage"])): reasons.append("Percentage is below the minimum requirement")
        if int(j["openings"]) <= 0: reasons.append("No openings are available")
        if j["min_passing_year"] and c["passing_year"] < j["min_passing_year"]: reasons.append("Passing year is below the required range")
        if j["max_passing_year"] and c["passing_year"] > j["max_passing_year"]: reasons.append("Passing year is above the required range")
        if c["backlog_count"] > (j["max_backlogs"] if j["max_backlogs"] is not None else 999): reasons.append("Backlog count exceeds the allowed maximum")
        if j["qualification"] and j["qualification"].lower() not in (c["qualification"] or "").lower(): reasons.append("Qualification does not match")
        if j["required_technology"] and j["required_technology"].lower() not in (c["primary_technology"] or "").lower():
            skill=Database.fetch_one("""SELECT cs.candidate_skill_id FROM candidate_skills cs JOIN skills s ON s.skill_id=cs.skill_id
                WHERE cs.candidate_id=%s AND LOWER(s.skill_name)=LOWER(%s)""",(candidate_id,j["required_technology"]))
            if not skill: reasons.append("Required technology does not match")
        return {"eligibility_status":"ELIGIBLE" if not reasons else "NOT_ELIGIBLE",
                "eligibility_reason":"Meets all configured criteria" if not reasons else "; ".join(reasons)}
