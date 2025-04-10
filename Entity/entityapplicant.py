from util.validator_util import validate_email
from exception.invalid_email_format import InvalidEmailFormat

class Applicant:
    def __init__(self, first_name, last_name, email, phone, resume, experience, applicant_id=None):
        try:
            validate_email(email)
        except InvalidEmailFormat as e:
            raise InvalidEmailFormat(e)

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.resume = resume
        self.experience = experience
        self.applicant_id = applicant_id


    def __str__(self):
        return f"[{self.applicant_id}] {self.first_name} {self.last_name} - {self.email}, Phone: {self.phone}, Experience: {self.experience} years"

    def __repr__(self):
        return self.__str__()