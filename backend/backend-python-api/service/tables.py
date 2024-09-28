from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import Tables
from config.database import database

table_collection: Collection = database['Tables']

def insert_table(_data: Tables) -> str:
    result = table_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def update_table(_data: Tables, table_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_table = table_collection.find_one({"_id": object_id})
    if not existing_table:
        raise HTTPException(status_code=404, detail="table not found")
    
    updated_table = table_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_table.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_table(table_id: str, table_collection: Collection):
    if not ObjectId.is_valid(table_id):
        raise HTTPException(status_code=400, detail="Invalid table ID")

    result = table_collection.delete_one({"_id": ObjectId(table_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="table not found")
    
    return {"message": "table deleted successfully"}
