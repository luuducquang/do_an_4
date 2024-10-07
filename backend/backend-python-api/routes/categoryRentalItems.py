from datetime import datetime
from typing import Optional
from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import CategoryRentalItems
from service.categoryRentalItems import delete_categoryrentalitem, insert_categoryrentalitem, update_categoryrentalitem


router = APIRouter()

categoryrentalitem_collection: Collection = database['CategoryRentalItems']

@router.get("/categoryrentalitems/get")
async def get_category():
    datas = []
    for data in categoryrentalitem_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.get("/categoryrentalitems/get/{category_id}")
async def get_category_by_id(category_id: str):
    if not ObjectId.is_valid(category_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    category = categoryrentalitem_collection.find_one({"_id": ObjectId(category_id)})

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    category["_id"] = str(category["_id"])
    return category

@router.post("/categoryrentalitems/search")
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

    total_items = categoryrentalitem_collection.count_documents(query)

    categoryRentalitems = categoryrentalitem_collection.find(query).skip(skip).limit(pageSize)

    data = []
    for category in categoryRentalitems:
        category["_id"] = str(category["_id"])
        data.append(category)

    return {
        "page":page,
        "pageSize":pageSize,
        "totalItems": total_items,
        "data": data,
    }

@router.post("/categoryrentalitems/add")
async def create_category(_data: CategoryRentalItems):
    _id = insert_categoryrentalitem(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/categoryrentalitems/update")
def edit_category(_data: CategoryRentalItems):
    result = update_categoryrentalitem(_data, categoryrentalitem_collection)
    return result

@router.delete("/categoryrentalitems/delete/{category_id}")
def remove_category(category_id: str):
    response = delete_categoryrentalitem(category_id, categoryrentalitem_collection)
    return response