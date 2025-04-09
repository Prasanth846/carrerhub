import re
class InvalidEmailException(Exception):
    """Custom exception for invalid email format."""
    pass

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailException(f"❌ Invalid email format: {email}")
