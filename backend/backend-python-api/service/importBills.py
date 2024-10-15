from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import ImportBills
from config.database import database

importbill_collection: Collection = database['ImportBills']

def ser_get_importbill():
    datas = []
    for data in importbill_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

def ser_insert_importbill(_data: ImportBills) -> str:
    result = importbill_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def ser_update_importbill(_data: ImportBills, importbill_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_importbill = importbill_collection.find_one({"_id": object_id})
    if not existing_importbill:
        raise HTTPException(status_code=404, detail="importbill not found")
    
    updated_importbill = importbill_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_importbill.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def ser_delete_importbill(importbill_id: str, importbill_collection: Collection):
    if not ObjectId.is_valid(importbill_id):
        raise HTTPException(status_code=400, detail="Invalid importbill ID")

    result = importbill_collection.delete_one({"_id": ObjectId(importbill_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="importbill not found")
    
    return {"message": "importbill deleted successfully"}
