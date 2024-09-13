from pydantic import BaseModel

class ProjectAllocationCreate(BaseModel):
    project_name: str
    employee_id: str
    role: str