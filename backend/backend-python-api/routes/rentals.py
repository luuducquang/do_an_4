from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Rentals
from service.rentals import ser_get_rental,ser_delete_rental, ser_insert_rental, ser_update_rental


router = APIRouter()

rental_collection: Collection = database['Rentals']

@router.get("/rentals/get")
async def get_rental():
    return ser_get_rental()

@router.post("/rentals/add")
async def create_rental(_data: Rentals):
    _id = ser_insert_rental(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/rentals/update")
def edit_rental(_data: Rentals):
    result = ser_update_rental(_data, rental_collection)
    return result

@router.delete("/rentals/delete/{rental_id}")
def remove_rental(rental_id: str):
    response = ser_delete_rental(rental_id, rental_collection)
    return response