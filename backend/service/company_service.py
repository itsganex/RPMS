from backend.dao.company_dao import CompanyDAO
from backend.util.validators import required
class CompanyService:
    dao=CompanyDAO()
    @classmethod
    def create(cls,data):
        required(data,"company_name","industry")
        return cls.dao.create(data)
