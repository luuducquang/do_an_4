from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Categorys
from service.category_service import insert_category


router = APIRouter()

category_collection: Collection = database['Categorys']

@router.get("/category/get")
async def get_categorys():
    datas = []
    for data in category_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/category/add")
async def create_product(_data: Categorys):
    _id = insert_category(_data)
    return {"message": "Created successfully", "_id": _id}