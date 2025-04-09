class SalaryNegativeException(Exception):
    def __init__(self, message="❌ Salary cannot be negative."):
        super().__init__(message)
