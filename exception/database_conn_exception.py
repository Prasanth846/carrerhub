class DatabaseConnException(Exception):
    def __init__(self, message="❌ Could not connect to the database."):
        super().__init__(message)