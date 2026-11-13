from backend.dao.base_dao import BaseDAO
class CompanyDAO(BaseDAO):
    table="companies"
    primary_key="company_id"
    allowed_columns=set(['company_name', 'industry', 'website', 'location', 'company_type', 'hr_name', 'hr_email', 'hr_mobile', 'status'])
