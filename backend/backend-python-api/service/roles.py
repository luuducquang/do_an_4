from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import Roles
from bson import ObjectId
from config.database import database

def insert_role(_data: Roles, role_collection: Collection):
    existing_role = role_collection.find_one({"role_name": _data.role_name})
    if existing_role:
        raise HTTPException(status_code=400, detail=f"Role with name '{_data.role_name}' already exists.")
    result =  role_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)


def update_role(_data: Roles, role_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_role = role_collection.find_one({"_id": object_id})
    if not existing_role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    updated_role = role_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_role.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_role(role_id: str, role_collection: Collection):
    if not ObjectId.is_valid(role_id):
        raise HTTPException(status_code=400, detail="Invalid role ID")

    result = role_collection.delete_one({"_id": ObjectId(role_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="not found")
    
    return {"message": "deleted successfully"}
