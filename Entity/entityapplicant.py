from util.validator_util import validate_email

class Applicant:
    def __init__(self, first_name, last_name, email, phone, resume, experience, applicant_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.resume = resume
        self.experience = experience
        self.applicant_id = applicant_id

        # Validate using the utility function
        validate_email(self.email)
