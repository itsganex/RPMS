from backend.service.application_service import ALLOWED
def test_rejected_is_terminal():
    assert not ALLOWED["REJECTED"]
