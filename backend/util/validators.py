import re
from backend.exception.custom_exceptions import ValidationError
def required(data, *fields):
    missing=[f for f in fields if data.get(f) in (None, "")]
    if missing: raise ValidationError("Required fields: " + ", ".join(missing))
def percentage(value):
    if value not in (None, "") and not 0 <= float(value) <= 100:
        raise ValidationError("Percentage must be between 0 and 100.")
def non_negative(value, field):
    if value not in (None, "") and int(value) < 0:
        raise ValidationError(f"{field} cannot be negative.")
def valid_email(value):
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value or ""):
        raise ValidationError("Enter a valid email address.")
