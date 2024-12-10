from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import SellItems
from config.database import database

sellitem_collection: Collection = database['SellItems']

def ser_get_sellitem():
    datas = []
    for data in sellitem_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

def ser_insert_sellitem(_data: SellItems) -> str:
    result = sellitem_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def ser_update_sellitem(_data: SellItems, sellitem_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_sellitem = sellitem_collection.find_one({"_id": object_id})
    if not existing_sellitem:
        raise HTTPException(status_code=404, detail="sellitem not found")
    
    updated_sellitem = sellitem_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_sellitem.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def ser_delete_sellitem(sellitem_id: str, sellitem_collection: Collection):
    if not ObjectId.is_valid(sellitem_id):
        raise HTTPException(status_code=400, detail="Invalid sellitem ID")

    result = sellitem_collection.delete_one({"_id": ObjectId(sellitem_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="sellitem not found")
    
    return {"message": "sellitem deleted successfully"}
