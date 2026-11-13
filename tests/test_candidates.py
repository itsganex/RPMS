import pytest
from backend.util.validators import percentage, non_negative
from backend.exception.custom_exceptions import ValidationError
def test_percentage_valid():
    percentage(78.5)
def test_percentage_invalid():
    with pytest.raises(ValidationError): percentage(101)
def test_backlog_negative():
    with pytest.raises(ValidationError): non_negative(-1,"Backlog count")
