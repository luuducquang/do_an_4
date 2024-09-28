from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import Bookings
from config.database import database

booking_collection: Collection = database['Bookings']

def insert_booking(_data: Bookings) -> str:
    result = booking_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def update_booking(_data: Bookings, booking_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_booking = booking_collection.find_one({"_id": object_id})
    if not existing_booking:
        raise HTTPException(status_code=404, detail="booking not found")
    
    updated_booking = booking_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_booking.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def delete_booking(booking_id: str, booking_collection: Collection):
    if not ObjectId.is_valid(booking_id):
        raise HTTPException(status_code=400, detail="Invalid booking ID")

    result = booking_collection.delete_one({"_id": ObjectId(booking_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="booking not found")
    
    return {"message": "booking deleted successfully"}
