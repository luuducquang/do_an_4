from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import ImportItems
from config.database import database

importitem_collection: Collection = database['ImportItems']

def insert_importitem(_data: ImportItems) -> str:
    result = importitem_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def update_importitem(_data: ImportItems, importitem_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_importitem = importitem_collection.find_one({"_id": object_id})
    if not existing_importitem:
        raise HTTPException(status_code=404, detail="importitem not found")
    
    updated_importitem = importitem_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_importitem.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_importitem(importitem_id: str, importitem_collection: Collection):
    if not ObjectId.is_valid(importitem_id):
        raise HTTPException(status_code=400, detail="Invalid importitem ID")

    result = importitem_collection.delete_one({"_id": ObjectId(importitem_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="importitem not found")
    
    return {"message": "importitem deleted successfully"}
