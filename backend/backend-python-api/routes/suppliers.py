from fastapi import APIRouter
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