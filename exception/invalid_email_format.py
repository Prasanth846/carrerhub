class InvalidEmailFormat(Exception):
    def __init__(self, message="Invalid email format. Must contain '@' and a domain."):
        super().__init__(message)
