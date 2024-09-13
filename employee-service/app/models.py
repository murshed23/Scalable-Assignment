from pydantic import BaseModel
from bson import ObjectId

class Employee(BaseModel):
    id: str
    name: str
    email: str
    job_title: str
    department: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}