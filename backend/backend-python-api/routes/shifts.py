from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Shifts
from service.shifts import delete_shift, insert_shift, update_shift


router = APIRouter()

shift_collection: Collection = database['Shifts']

@router.get("/shifts/get")
async def get_shift():
    datas = []
    for data in shift_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/shifts/add")
async def create_shift(_data: Shifts):
    _id = insert_shift(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/shifts/update")
def edit_shift(_data: Shifts):
    result = update_shift(_data, shift_collection)
    return result

@router.delete("/shifts/delete/{shift_id}")
def remove_shift(shift_id: str):
    response = delete_shift(shift_id, shift_collection)
    return response