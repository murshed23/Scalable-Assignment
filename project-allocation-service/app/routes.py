from fastapi import APIRouter, HTTPException
from app.models import ProjectAllocation
from app.schemas import ProjectAllocationCreate
from app.database import get_project_allocation_collection
from bson import ObjectId

router = APIRouter()

# Create a project allocation
@router.post("/", response_model=ProjectAllocation)
async def create_project_allocation(allocation: ProjectAllocationCreate):
    allocation_dict = allocation.dict()
    result = await get_project_allocation_collection().insert_one(allocation_dict)
    allocation_dict["id"] = str(result.inserted_id)
    return ProjectAllocation(**allocation_dict)

# Get a project allocation by ID
@router.get("/{allocation_id}", response_model=ProjectAllocation)
async def read_project_allocation(allocation_id: str):
    allocation = await get_project_allocation_collection().find_one({"_id": ObjectId(allocation_id)})
    if allocation:
        return ProjectAllocation(**allocation)
    raise HTTPException(status_code=404, detail="Project allocation not found")

# Update a project allocation
@router.put("/{allocation_id}", response_model=ProjectAllocation)
async def update_project_allocation(allocation_id: str, allocation: ProjectAllocationCreate):
    update_result = await get_project_allocation_collection().update_one(
        {"_id": ObjectId(allocation_id)}, {"$set": allocation.dict()}
    )
    if update_result.modified_count == 1:
        updated_allocation = await get_project_allocation_collection().find_one({"_id": ObjectId(allocation_id)})
        if updated_allocation:
            return ProjectAllocation(**updated_allocation)
    raise HTTPException(status_code=404, detail="Project allocation not found")

# Delete a project allocation
@router.delete("/{allocation_id}", response_model=dict)
async def delete_project_allocation(allocation_id: str):
    delete_result = await get_project_allocation_collection().delete_one({"_id": ObjectId(allocation_id)})
    if delete_result.deleted_count == 1:
        return {"status": "Project allocation deleted"}
    raise HTTPException(status_code=404, detail="Project allocation not found")