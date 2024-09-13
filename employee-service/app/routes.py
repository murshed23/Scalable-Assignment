from fastapi import APIRouter, HTTPException
from app.models import Employee
from app.schemas import EmployeeCreate
from app.database import get_employee_collection
from bson import ObjectId

router = APIRouter()

# Create an employee
@router.post("/", response_model=Employee)
async def create_employee(employee: EmployeeCreate):
    employee_dict = employee.dict()
    result = await get_employee_collection().insert_one(employee_dict)
    employee_dict["id"] = str(result.inserted_id)
    return Employee(**employee_dict)

# Get an employee by ID
@router.get("/{employee_id}", response_model=Employee)
async def read_employee(employee_id: str):
    employee = await get_employee_collection().find_one({"_id": ObjectId(employee_id)})
    if employee:
        employee["id"] = employee_id
        return Employee(**employee)
    raise HTTPException(status_code=404, detail="Employee not found")

# Update an employee
@router.put("/{employee_id}", response_model=Employee)
async def update_employee(employee_id: str, employee: EmployeeCreate):
    update_result = await get_employee_collection().update_one(
        {"_id": ObjectId(employee_id)}, {"$set": employee.dict()}
    )
    if update_result.modified_count == 1:
        updated_employee = await get_employee_collection().find_one({"_id": ObjectId(employee_id)})
        if updated_employee:
            updated_employee["id"] = employee_id
            return Employee(**updated_employee)
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete an employee
@router.delete("/{employee_id}", response_model=dict)
async def delete_employee(employee_id: str):
    delete_result = await get_employee_collection().delete_one({"_id": ObjectId(employee_id)})
    if delete_result.deleted_count == 1:
        return {"status": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")