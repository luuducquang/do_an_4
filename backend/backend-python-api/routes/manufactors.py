from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Manufactors
from service.manufactor import delete_manufactor, insert_manufactor, update_manufactor


router = APIRouter()

manufactor_collection: Collection = database['Manufactors']

@router.get("/manufactors/get")
async def get_manufactor():
    datas = []
    for data in manufactor_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/manufactors/add")
async def create_manufactor(_data: Manufactors):
    _id = insert_manufactor(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/manufactors/update")
def edit_manufactor(_data: Manufactors):
    result = update_manufactor(_data, manufactor_collection)
    return result

@router.delete("/manufactors/delete/{manufactor_id}")
def remove_manufactor(manufactor_id: str):
    response = delete_manufactor(manufactor_id, manufactor_collection)
    return response