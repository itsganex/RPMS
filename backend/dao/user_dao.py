from backend.dao.base_dao import BaseDAO


class UserDAO(BaseDAO):
    table = "users"
    primary_key = "user_id"
    allowed_columns = {
        "username", "password_hash", "full_name", "email",
        "mobile", "role_id", "candidate_id", "status"
    }
