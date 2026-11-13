import re
import uuid
from datetime import date
from decimal import Decimal, InvalidOperation

from werkzeug.security import generate_password_hash, check_password_hash

from backend.database import Database, get_connection
from backend.exception.custom_exceptions import AuthenticationError


class AuthService:
    @staticmethod
    def login(identifier, password, role=None):
        identifier = (identifier or "").strip()
        if not identifier or not password:
            raise AuthenticationError("Enter your username, email or mobile number and password.")

        sql = """
            SELECT u.user_id, u.username, u.password_hash, u.full_name,
                   u.email, u.mobile, u.candidate_id, u.status, r.role_code
            FROM users u
            JOIN roles r ON r.role_id = u.role_id
            WHERE (u.username = %s OR u.email = %s OR u.mobile = %s)
              AND u.status = 'ACTIVE'
              AND r.is_active = 1
        """
        params = [identifier, identifier, identifier]
        if role:
            sql += " AND r.role_code = %s"
            params.append(role)

        row = Database.fetch_one(sql, tuple(params))
        if not row or not check_password_hash(row["password_hash"], password):
            raise AuthenticationError("Invalid login details. Check your credentials and selected role.")

        Database.execute(
            "UPDATE users SET last_login_at = NOW() WHERE user_id = %s",
            (row["user_id"],)
        )

        return {
            "user_id": row["user_id"],
            "username": row["username"],
            "full_name": row["full_name"],
            "role": row["role_code"],
            "candidate_id": row["candidate_id"]
        }

    @staticmethod
    def register_student(data):
        required_fields = [
            "full_name", "date_of_birth", "gender", "parent_guardian_name",
            "mobile", "email", "course", "branch", "class_grade",
            "college", "passing_year", "password"
        ]
        missing = [field for field in required_fields if not str(data.get(field, "")).strip()]
        if missing:
            raise ValueError("Please complete all required fields.")

        full_name = str(data["full_name"]).strip()
        email = str(data["email"]).strip().lower()
        mobile = re.sub(r"\D", "", str(data["mobile"]))
        password = str(data["password"])

        if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
            raise ValueError("Enter a valid email address.")
        if not re.fullmatch(r"\d{10}", mobile):
            raise ValueError("Enter a valid 10-digit Indian mobile number.")
        if len(password) < 8:
            raise ValueError("Password must contain at least 8 characters.")

        try:
            birth_date = date.fromisoformat(str(data["date_of_birth"]))
        except ValueError:
            raise ValueError("Enter a valid date of birth.")
        if birth_date > date.today():
            raise ValueError("Date of birth must be in the past.")

        try:
            passing_year = int(data["passing_year"])
            if not 1990 <= passing_year <= 2100:
                raise ValueError
        except (TypeError, ValueError):
            raise ValueError("Enter a valid passing year.")

        def optional_number(field, label, minimum=None, maximum=None):
            value = data.get(field)
            if value in (None, ""):
                return None
            try:
                number = Decimal(str(value))
            except (InvalidOperation, TypeError):
                raise ValueError(f"{label} must be a valid number.")
            if minimum is not None and number < Decimal(str(minimum)):
                raise ValueError(f"{label} cannot be less than {minimum}.")
            if maximum is not None and number > Decimal(str(maximum)):
                raise ValueError(f"{label} cannot be greater than {maximum}.")
            return number

        semester = optional_number("semester", "Semester", 1, 12)
        if semester is not None and semester != semester.to_integral_value():
            raise ValueError("Semester must be a whole number.")

        tenth = optional_number("tenth_percentage", "10th percentage", 0, 100)
        twelfth = optional_number("twelfth_percentage", "12th percentage", 0, 100)
        percentage = optional_number("percentage", "Graduation percentage", 0, 100)
        cgpa = optional_number("cgpa", "CGPA", 0, 10)
        expected_salary = optional_number("expected_salary", "Expected salary", 0, None)

        try:
            backlog_count = int(data.get("backlog_count") or 0)
            if backlog_count < 0:
                raise ValueError
        except (TypeError, ValueError):
            raise ValueError("Backlog count must be zero or a positive whole number.")

        # Keep usernames unique while allowing students to sign in with their mobile number.
        username = f"STU{mobile}"
        candidate_code = f"CAN-{date.today().year}-{uuid.uuid4().hex[:8].upper()}"
        password_hash = generate_password_hash(password)

        candidate_values = {
            "candidate_code": candidate_code,
            "full_name": full_name,
            "parent_guardian_name": str(data["parent_guardian_name"]).strip(),
            "email": email,
            "mobile": mobile,
            "date_of_birth": birth_date,
            "gender": str(data["gender"]).strip(),
            "qualification": str(data["course"]).strip(),
            "course": str(data["course"]).strip(),
            "branch": str(data["branch"]).strip(),
            "class_grade": str(data["class_grade"]).strip(),
            "semester": int(semester) if semester is not None else None,
            "college": str(data["college"]).strip(),
            "university": (str(data.get("university") or "").strip() or None),
            "passing_year": passing_year,
            "tenth_percentage": tenth,
            "twelfth_percentage": twelfth,
            "percentage": percentage,
            "cgpa": cgpa,
            "backlog_count": backlog_count,
            "primary_technology": (str(data.get("primary_technology") or "").strip() or None),
            "secondary_skills": (str(data.get("secondary_skills") or "").strip() or None),
            "programming_languages": (str(data.get("programming_languages") or "").strip() or None),
            "frameworks": (str(data.get("frameworks") or "").strip() or None),
            "database_skills": (str(data.get("database_skills") or "").strip() or None),
            "skill_level": (str(data.get("skill_level") or "").strip() or None),
            "current_location": (str(data.get("current_location") or "").strip() or None),
            "preferred_job_role": (str(data.get("preferred_job_role") or "").strip() or None),
            "preferred_location": (str(data.get("preferred_location") or "").strip() or None),
            "expected_salary": expected_salary,
            "willing_to_relocate": (str(data.get("willing_to_relocate") or "").strip() or None),
            "internship_experience": (str(data.get("internship_experience") or "").strip() or None),
            "work_experience": (str(data.get("work_experience") or "").strip() or None),
            "profile_status": "ACTIVE",
            "placement_status": "NOT_PLACED"
        }

        def create_account(conn, cur):
            cur.execute(
                """INSERT INTO roles (role_code, role_name, is_active)
                   VALUES ('STUDENT', 'Student', 1)
                   ON DUPLICATE KEY UPDATE role_name = VALUES(role_name), is_active = 1"""
            )
            cur.execute("SELECT role_id FROM roles WHERE role_code = 'STUDENT'")
            role_row = cur.fetchone()
            if not role_row:
                raise RuntimeError("Student role could not be created.")

            columns = list(candidate_values.keys())
            placeholders = ", ".join(["%s"] * len(columns))
            cur.execute(
                f"INSERT INTO candidates ({', '.join(columns)}) VALUES ({placeholders})",
                tuple(candidate_values[column] for column in columns)
            )
            candidate_id = cur.lastrowid

            cur.execute(
                """INSERT INTO users
                   (username, password_hash, full_name, email, mobile, role_id, candidate_id, status)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, 'ACTIVE')""",
                (username, password_hash, full_name, email, mobile, role_row["role_id"], candidate_id)
            )
            user_id = cur.lastrowid
            return {"candidate_id": candidate_id, "user_id": user_id, "candidate_code": candidate_code}

        try:
            result = Database.transaction(create_account)
        except Exception as exc:
            # Do not expose database details or SQL text to the browser.
            error_text = str(exc).lower()
            if "duplicate" in error_text or "1062" in error_text:
                raise ValueError("An account with this email or mobile number already exists.") from exc
            raise

        return result
