from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import BillSells
from service.billSells import ser_get_billsell,ser_delete_billsell, ser_insert_billsell, ser_update_billsell


router = APIRouter()

billsell_collection: Collection = database['BillSells']

@router.get("/billsells/get")
async def get_billsell():
    return ser_get_billsell()

@router.post("/billsells/add")
async def create_billsell(_data: BillSells):
    _id = ser_insert_billsell(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/billsells/update")
def edit_billsell(_data: BillSells):
    result = ser_update_billsell(_data, billsell_collection)
    return result

@router.delete("/billsells/delete/{billsell_id}")
def remove_billsell(billsell_id: str):
    response = ser_delete_billsell(billsell_id, billsell_collection)
    return response