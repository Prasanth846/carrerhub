class Jobs:
    def __init__(self, job_id, job_title, job_description, job_location, salary, job_type, posted_date):
        self.job_id = job_id
        self.job_title = job_title
        self.job_description = job_description
        self.job_location = job_location
        self.salary = salary
        self.job_type = job_type
        self.posted_date = posted_date

    def __str__(self):
        return f"[{self.job_id}] {self.job_title} | {self.job_location} | ₹{self.salary} | {self.job_type} | Posted: {self.posted_date.strftime('%Y-%m-%d')}"
