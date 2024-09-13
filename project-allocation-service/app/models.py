from pydantic import BaseModel
from bson import ObjectId

class ProjectAllocation(BaseModel):
    id: str = None
    project_name: str
    employee_id: str
    role: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}