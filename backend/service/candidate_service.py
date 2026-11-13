
from backend.dao.candidate_dao import CandidateDAO
from backend.util.validators import (
    required,
    percentage,
    non_negative,
    valid_email
)
from backend.util.id_generator import business_code
from backend.util.logger import log_activity
from backend.database import get_connection


class CandidateService:

    dao = CandidateDAO()

    @classmethod
    def create(cls, data, user_id=None):

        # Validate candidate details
        required(
            data,
            "full_name",
            "email",
            "mobile",
            "qualification",
            "passing_year"
        )

        valid_email(data["email"])
        percentage(data.get("percentage"))
        non_negative(
            data.get("backlog_count", 0),
            "Backlog count"
        )

        # Establish database connection
        conn = get_connection()
        cur = None

        try:
            cur = conn.cursor()

            # Generate candidate code
            cur.execute(
                "SELECT COALESCE(MAX(candidate_id), 0) + 1 FROM candidates"
            )

            n = cur.fetchone()[0]
            data["candidate_code"] = business_code("CAN", n)

            # Select only allowed columns
            clean = {
                key: value
                for key, value in data.items()
                if key in cls.dao.allowed_columns
            }

            if not clean:
                raise ValueError("No valid candidate details supplied.")

            # Prepare SQL query
            columns = ", ".join(clean.keys())
            placeholders = ", ".join(["%s"] * len(clean))

            sql = (
                f"INSERT INTO candidates ({columns}) "
                f"VALUES ({placeholders})"
            )

            # Insert candidate
            cur.execute(sql, tuple(clean.values()))

            candidate_id = cur.lastrowid

            # Save changes
            conn.commit()

            # Record activity
            log_activity(
                f"Candidate Created: {data['candidate_code']}",
                user_id
            )

            return candidate_id

        except Exception:
            conn.rollback()
            raise

        finally:
            if cur is not None:
                cur.close()

            conn.close()

    @classmethod
    def update(cls, cid, data):

        # Validate updated details
        percentage(data.get("percentage"))
        non_negative(
            data.get("backlog_count"),
            "Backlog count"
        )

        return cls.dao.update(cid, data)
