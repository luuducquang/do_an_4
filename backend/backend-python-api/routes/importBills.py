from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import ImportBills
from service.importBills import delete_importbill, insert_importbill, update_importbill


router = APIRouter()

importbill_collection: Collection = database['ImportBills']

@router.get("/importbills/get")
async def get_importbill():
    datas = []
    for data in importbill_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/importbills/add")
async def create_importbill(_data: ImportBills):
    _id = insert_importbill(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/importbills/update")
def edit_importbill(_data: ImportBills):
    result = update_importbill(_data, importbill_collection)
    return result

@router.delete("/importbills/delete/{importbill_id}")
def remove_importbill(importbill_id: str):
    response = delete_importbill(importbill_id, importbill_collection)
    return response