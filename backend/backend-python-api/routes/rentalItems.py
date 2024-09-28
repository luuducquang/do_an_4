from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import RentalItems
from service.rentalItems import delete_rentalitem, insert_rentalitem, update_rentalitem


router = APIRouter()

rentalitem_collection: Collection = database['RentalItems']

@router.get("/rentalitems/get")
async def get_rentalitem():
    datas = []
    for data in rentalitem_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/rentalitems/add")
async def create_rentalitem(_data: RentalItems):
    _id = insert_rentalitem(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/rentalitems/update")
def edit_rentalitem(_data: RentalItems):
    result = update_rentalitem(_data, rentalitem_collection)
    return result

@router.delete("/rentalitems/delete/{rentalitem_id}")
def remove_rentalitem(rentalitem_id: str):
    response = delete_rentalitem(rentalitem_id, rentalitem_collection)
    return response