from datetime import datetime
from typing import Optional
from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException
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

@router.get("/categorys/get/{category_id}")
async def get_category_by_id(category_id: str):
    if not ObjectId.is_valid(category_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    category = category_collection.find_one({"_id": ObjectId(category_id)})

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    category["_id"] = str(category["_id"])
    return category

@router.post("/categorys/search")
async def search_category(
    page: int = Body(...),
    pageSize: int = Body(...),
    category_name: Optional[str] = Body(None)
):
    if page <= 0 or pageSize <= 0:
        raise HTTPException(status_code=400, detail="Page and pageSize must be greater than 0")
    
    skip = (page - 1) * pageSize

    query = {}
    if category_name:
        query["category_name"] = {"$regex": category_name, "$options": "i"}

    total_items = category_collection.count_documents(query)

    categorys = category_collection.find(query).skip(skip).limit(pageSize)

    data = []
    for category in categorys:
        category["_id"] = str(category["_id"])
        data.append(category)

    return {
        "page":page,
        "pageSize":pageSize,
        "totalItems": total_items,
        "data": data,
    }

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