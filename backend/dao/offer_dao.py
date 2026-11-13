from backend.dao.base_dao import BaseDAO
class OfferDAO(BaseDAO):
    table="offers"
    primary_key="offer_id"
    allowed_columns=set(['offer_code', 'application_id', 'designation', 'offered_package', 'offer_date', 'expected_joining_date', 'offer_status'])
