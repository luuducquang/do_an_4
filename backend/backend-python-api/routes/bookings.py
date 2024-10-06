from typing import Optional
from fastapi import APIRouter, Body, HTTPException, Query
from pymongo.collection import Collection
from config.database import database
from datetime import datetime
from schemas.schemas import Bookings
from service.bookings import delete_booking, insert_booking, update_booking


router = APIRouter()

booking_collection: Collection = database['Bookings']

@router.get("/bookings/get")
async def get_booking():
    datas = []
    for data in booking_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/bookings/search")
async def search_booking(
    page: int = Body(...),
    pageSize: int = Body(...),
    user_id: Optional[str] = Body(None),
    table_id: Optional[str] = Body(None),
    booking_date: Optional[datetime] = Body(None),
    start_time: Optional[datetime] = Body(None),
    end_time: Optional[datetime] = Body(None),
    status: Optional[bool] = Body(None)
):
    if page <= 0 or pageSize <= 0:
        raise HTTPException(status_code=400, detail="Page and pageSize must be greater than 0")
    
    skip = (page - 1) * pageSize

    query = {}
    if user_id:
        query["user_id"] = user_id
    if table_id:
        query["table_id"] = table_id
    if booking_date:
        query["booking_date"] = booking_date
    if start_time:
        query["start_time"] = start_time
    if end_time:
        query["end_time"] = end_time
    if status is not None:
        query["status"] = status

    total_items = booking_collection.count_documents(query)

    bookings = booking_collection.find(query).skip(skip).limit(pageSize)

    data = []
    for booking in bookings:
        booking["_id"] = str(booking["_id"])
        data.append(booking)

    return {
        "page":page,
        "pageSize":pageSize,
        "totalItems": total_items,
        "data": data,
    }

@router.post("/bookings/add")
async def create_booking(_data: Bookings):
    _id = insert_booking(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/bookings/update")
def edit_booking(_data: Bookings):
    result = update_booking(_data, booking_collection)
    return result

@router.delete("/bookings/delete/{booking_id}")
def remove_booking(booking_id: str):
    response = delete_booking(booking_id, booking_collection)
    return response