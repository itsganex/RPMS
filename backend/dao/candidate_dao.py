from backend.dao.base_dao import BaseDAO


class CandidateDAO(BaseDAO):
    table = "candidates"
    primary_key = "candidate_id"
    allowed_columns = {
        "candidate_code", "full_name", "parent_guardian_name", "email", "mobile",
        "date_of_birth", "gender", "qualification", "course", "branch",
        "class_grade", "semester", "college", "university", "passing_year",
        "tenth_percentage", "twelfth_percentage", "percentage", "cgpa",
        "backlog_count", "primary_technology", "secondary_skills",
        "programming_languages", "frameworks", "database_skills", "skill_level",
        "current_location", "preferred_job_role", "preferred_location",
        "expected_salary", "willing_to_relocate", "internship_experience",
        "work_experience", "profile_status", "placement_status"
    }

