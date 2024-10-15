from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import Bookings, Searchs
from config.database import database

booking_collection: Collection = database['Bookings']

def ser_get_booking():
    datas = []
    for data in booking_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

def ser_search_booking(_data:Searchs):
    if _data.page <= 0 or _data.pageSize <= 0:
        raise HTTPException(status_code=400, detail="Page and pageSize must be greater than 0")
    
    skip = (_data.page - 1) * _data.pageSize

    query = {}
    if _data.search_term:
        query["$or"] = [
            {"booking_date": {"$regex": _data.search_term, "$options": "i"}},
            {"start_time": {"$regex": _data.search_term, "$options": "i"}},
            {"end_time": {"$regex": _data.search_term, "$options": "i"}},
            {"status": {"$regex": _data.search_term, "$options": "i"}},
        ]

    total_items = booking_collection.count_documents(query)

    bookings = booking_collection.find(query).skip(skip).limit(_data.pageSize)

    data = []
    for booking in bookings:
        booking["_id"] = str(booking["_id"])
        data.append(booking)

    return {
        "page":_data.page,
        "pageSize":_data.pageSize,
        "totalItems": total_items,
        "data": data,
    }

def ser_insert_booking(_data: Bookings) -> str:
    result = booking_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def ser_update_booking(_data: Bookings, booking_collection: Collection):
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


def ser_delete_booking(booking_id: str, booking_collection: Collection):
    if not ObjectId.is_valid(booking_id):
        raise HTTPException(status_code=400, detail="Invalid booking ID")

    result = booking_collection.delete_one({"_id": ObjectId(booking_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="booking not found")
    
    return {"message": "booking deleted successfully"}
