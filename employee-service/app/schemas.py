from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    email: str
    job_title: str
    department: str