from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import OrderItems
from config.database import database

orderitem_collection: Collection = database['OrderItems']

def insert_orderitem(_data: OrderItems) -> str:
    result = orderitem_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def update_orderitem(_data: OrderItems, orderitem_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_orderitem = orderitem_collection.find_one({"_id": object_id})
    if not existing_orderitem:
        raise HTTPException(status_code=404, detail="orderitem not found")
    
    updated_orderitem = orderitem_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_orderitem.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_orderitem(orderitem_id: str, orderitem_collection: Collection):
    if not ObjectId.is_valid(orderitem_id):
        raise HTTPException(status_code=400, detail="Invalid orderitem ID")

    result = orderitem_collection.delete_one({"_id": ObjectId(orderitem_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="orderitem not found")
    
    return {"message": "orderitem deleted successfully"}
