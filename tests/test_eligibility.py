from backend.service.application_service import ALLOWED
def test_applied_cannot_jump_to_joined():
    assert "JOINED" not in ALLOWED["APPLIED"]
def test_selected_can_be_offered():
    assert "OFFERED" in ALLOWED["SELECTED"]
