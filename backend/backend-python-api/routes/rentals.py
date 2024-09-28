from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Rentals
from service.rentals import delete_rental, insert_rental, update_rental


router = APIRouter()

rental_collection: Collection = database['Rentals']

@router.get("/rentals/get")
async def get_rental():
    datas = []
    for data in rental_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/rentals/add")
async def create_rental(_data: Rentals):
    _id = insert_rental(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/rentals/update")
def edit_rental(_data: Rentals):
    result = update_rental(_data, rental_collection)
    return result

@router.delete("/rentals/delete/{rental_id}")
def remove_rental(rental_id: str):
    response = delete_rental(rental_id, rental_collection)
    return response