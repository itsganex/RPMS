from backend.dao.base_dao import BaseDAO
class PlacementDAO(BaseDAO):
    table="placements"
    primary_key="placement_id"
    allowed_columns=set(['offer_id', 'candidate_id', 'company_id', 'actual_joining_date', 'joining_status', 'final_package', 'designation'])
