from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import ImportBills
from service.importBills import ser_get_importbill,ser_delete_importbill, ser_insert_importbill, ser_update_importbill


router = APIRouter()

importbill_collection: Collection = database['ImportBills']

@router.get("/importbills/get")
async def get_importbill():
    return ser_get_importbill()

@router.post("/importbills/add")
async def create_importbill(_data: ImportBills):
    _id = ser_insert_importbill(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/importbills/update")
def edit_importbill(_data: ImportBills):
    result = ser_update_importbill(_data, importbill_collection)
    return result

@router.delete("/importbills/delete/{importbill_id}")
def remove_importbill(importbill_id: str):
    response = ser_delete_importbill(importbill_id, importbill_collection)
    return response