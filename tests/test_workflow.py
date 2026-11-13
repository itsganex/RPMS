import pytest
from backend.service.application_service import ALLOWED
def test_workflow_has_terminal_states():
    assert ALLOWED["JOINED"] == set()
    assert ALLOWED["REJECTED"] == set()
def test_applied_to_shortlisted_requires_verification():
    assert "SHORTLISTED" not in ALLOWED["APPLIED"]
    assert "ELIGIBILITY_VERIFIED" in ALLOWED["APPLIED"]
