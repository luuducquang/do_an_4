from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import News
from service.news import delete_new, insert_new, update_new


router = APIRouter()

new_collection: Collection = database['News']

@router.get("/news/get")
async def get_new():
    datas = []
    for data in new_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/news/add")
async def create_new(_data: News):
    _id = insert_new(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/news/update")
def edit_new(_data: News):
    result = update_new(_data, new_collection)
    return result

@router.delete("/news/delete/{new_id}")
def remove_new(new_id: str):
    response = delete_new(new_id, new_collection)
    return response