from typing import Optional
from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Suppliers
from service.suppliers import delete_supplier, insert_supplier, update_supplier


router = APIRouter()

supplier_collection: Collection = database['Suppliers']

@router.get("/suppliers/get")
async def get_supplier():
    datas = []
    for data in supplier_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.get("/suppliers/get/{supplier_id}")
async def get_supplier_by_id(supplier_id: str):
    if not ObjectId.is_valid(supplier_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    supplier = supplier_collection.find_one({"_id": ObjectId(supplier_id)})

    if supplier is None:
        raise HTTPException(status_code=404, detail="supplier not found")

    supplier["_id"] = str(supplier["_id"])
    return supplier

@router.post("/suppliers/search")
async def search_supplier(
    page: int = Body(...),
    pageSize: int = Body(...),
    name: Optional[str] = Body(None)
):
    if page <= 0 or pageSize <= 0:
        raise HTTPException(status_code=400, detail="Page and pageSize must be greater than 0")
    
    skip = (page - 1) * pageSize

    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    total_items = supplier_collection.count_documents(query)

    suppliers = supplier_collection.find(query).skip(skip).limit(pageSize)

    data = []
    for supplier in suppliers:
        supplier["_id"] = str(supplier["_id"])
        data.append(supplier)

    return {
        "page":page,
        "pageSize":pageSize,
        "totalItems": total_items,
        "data": data,
    }

@router.post("/suppliers/add")
async def create_supplier(_data: Suppliers):
    _id = insert_supplier(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/suppliers/update")
def edit_supplier(_data: Suppliers):
    result = update_supplier(_data, supplier_collection)
    return result

@router.delete("/suppliers/delete/{supplier_id}")
def remove_supplier(supplier_id: str):
    response = delete_supplier(supplier_id, supplier_collection)
    return response