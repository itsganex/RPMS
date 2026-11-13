from datetime import date
def business_code(prefix, number):
    return f"{prefix}-{date.today().year}-{int(number):04d}"
