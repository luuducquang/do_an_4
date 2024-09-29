from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import PricingRules
from config.database import database

pricingrule_collection: Collection = database['PricingRules']

def insert_pricingrule(_data: PricingRules) -> str:
    result = pricingrule_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def update_pricingrule(_data: PricingRules, pricingrule_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_pricingrule = pricingrule_collection.find_one({"_id": object_id})
    if not existing_pricingrule:
        raise HTTPException(status_code=404, detail="pricingrule not found")
    
    updated_pricingrule = pricingrule_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_pricingrule.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_pricingrule(pricingrule_id: str, pricingrule_collection: Collection):
    if not ObjectId.is_valid(pricingrule_id):
        raise HTTPException(status_code=400, detail="Invalid pricingrule ID")

    result = pricingrule_collection.delete_one({"_id": ObjectId(pricingrule_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="pricingrule not found")
    
    return {"message": "pricingrule deleted successfully"}
