class DeadlineOverException(Exception):
    def __init__(self, message="❌ Application deadline is over. You can't apply for this job."):
        super().__init__(message)
