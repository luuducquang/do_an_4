from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import BillSells
from config.database import database

billsell_collection: Collection = database['BillSells']

def ser_get_billsell():
    datas = []
    for data in billsell_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

def ser_insert_billsell(_data: BillSells) -> str:
    result = billsell_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def ser_update_billsell(_data: BillSells, billsell_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_billsell = billsell_collection.find_one({"_id": object_id})
    if not existing_billsell:
        raise HTTPException(status_code=404, detail="billsell not found")
    
    updated_billsell = billsell_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_billsell.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def ser_delete_billsell(billsell_id: str, billsell_collection: Collection):
    if not ObjectId.is_valid(billsell_id):
        raise HTTPException(status_code=400, detail="Invalid billsell ID")

    result = billsell_collection.delete_one({"_id": ObjectId(billsell_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="billsell not found")
    
    return {"message": "billsell deleted successfully"}
