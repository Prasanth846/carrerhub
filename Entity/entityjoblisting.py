class Jobs:
    def __init__(self,company_id,job_title,job_desc,job_location,salary,job_type,posted_date,deadline,job_id=None):
        self.job_id=job_id
        self.company_id=company_id
        self.job_title=job_title
        self.job_desc=job_desc
        self.job_location=job_location
        self.salary=salary
        self.job_type=job_type
        self.posted_date=posted_date
        self.deadline=deadline