from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Categorys
from service.categorys import delete_category, insert_category, update_category


router = APIRouter()

category_collection: Collection = database['Categorys']

@router.get("/categorys/get")
async def get_category():
    datas = []
    for data in category_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/categorys/add")
async def create_category(_data: Categorys):
    _id = insert_category(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/categorys/update")
def edit_category(_data: Categorys):
    result = update_category(_data, category_collection)
    return result

@router.delete("/categorys/delete/{category_id}")
def remove_category(category_id: str):
    response = delete_category(category_id, category_collection)
    return response