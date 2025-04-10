import re
from exception.invalid_email_format import InvalidEmailFormat

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailFormat(f"❌ Invalid email format: {email}")
