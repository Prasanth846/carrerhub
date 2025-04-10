class Company:
    def __init__(self, company_id=None, company_name="", location=""):
        self.company_id = company_id
        self.company_name = company_name
        self.location = location

    def __str__(self):
        return f"[{self.company_id}] {self.company_name} - {self.location}"

    def __repr__(self):
        return self.__str__()


