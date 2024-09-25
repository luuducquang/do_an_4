from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import Employees
from config.database import database

employee_collection: Collection = database['Employees']

def insert_employee(_data: Employees) -> str:
    result = employee_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def update_employee(_data: Employees, employee_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_employee = employee_collection.find_one({"_id": object_id})
    if not existing_employee:
        raise HTTPException(status_code=404, detail="employee not found")
    
    updated_employee = employee_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_employee.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_employee(employee_id: str, employee_collection: Collection):
    if not ObjectId.is_valid(employee_id):
        raise HTTPException(status_code=400, detail="Invalid employee ID")

    result = employee_collection.delete_one({"_id": ObjectId(employee_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="employee not found")
    
    return {"message": "employee deleted successfully"}
