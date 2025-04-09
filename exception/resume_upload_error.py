class ResumeUploadError(Exception):
    def __init__(self, message="Resume upload failed."):
        super().__init__(message)
