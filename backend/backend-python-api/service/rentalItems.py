from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import RentalItems
from config.database import database

rentalitem_collection: Collection = database['RentalItems']

def insert_rentalitem(_data: RentalItems) -> str:
    result = rentalitem_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def update_rentalitem(_data: RentalItems, rentalitem_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_rentalitem = rentalitem_collection.find_one({"_id": object_id})
    if not existing_rentalitem:
        raise HTTPException(status_code=404, detail="rentalitem not found")
    
    updated_rentalitem = rentalitem_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_rentalitem.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_rentalitem(rentalitem_id: str, rentalitem_collection: Collection):
    if not ObjectId.is_valid(rentalitem_id):
        raise HTTPException(status_code=400, detail="Invalid rentalitem ID")

    result = rentalitem_collection.delete_one({"_id": ObjectId(rentalitem_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="rentalitem not found")
    
    return {"message": "rentalitem deleted successfully"}
