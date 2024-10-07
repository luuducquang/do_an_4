from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import CategoryRentalItems
from config.database import database

categoryrentalitem_collection: Collection = database['CategoryRentalItems']

def insert_categoryrentalitem(_data: CategoryRentalItems) -> str:
    result = categoryrentalitem_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def update_categoryrentalitem(_data: CategoryRentalItems, categoryrentalitem_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_category = categoryrentalitem_collection.find_one({"_id": object_id})
    if not existing_category:
        raise HTTPException(status_code=404, detail="category not found")
    
    updated_category = categoryrentalitem_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_category.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_categoryrentalitem(category_id: str, categoryrentalitem_collection: Collection):
    if not ObjectId.is_valid(category_id):
        raise HTTPException(status_code=400, detail="Invalid category ID")

    result = categoryrentalitem_collection.delete_one({"_id": ObjectId(category_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="category not found")
    
    return {"message": "category deleted successfully"}
