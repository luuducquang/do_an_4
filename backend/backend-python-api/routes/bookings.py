from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
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