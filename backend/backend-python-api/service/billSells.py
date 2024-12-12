from typing import List
from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import BillSells
from config.database import database

billsell_collection: Collection = database['BillSells']
sellitem_collection: Collection = database['SellItems']
rentalitem_collection: Collection = database['RentalItems']

def ser_get_billsell():
    datas = []
    for data in billsell_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

def ser_get_billsell_by_user(user_id: str):
    datas = []
    for data in billsell_collection.find({"user_id": user_id}):
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

def ser_get_billsell_by_sell_id(sell_id: str):
    datas = []
    for data in sellitem_collection.find({"sell_id": sell_id}):
        data["_id"] = str(data["_id"])
        rental_item_data = rentalitem_collection.find_one({"_id": ObjectId(data["item_id"])})
        if rental_item_data:
            rental_item_data["_id"] = str(rental_item_data["_id"])  
            data["rentalitem"] = rental_item_data  
        else:
            data["rentalitem"] = None  
        datas.append(data)
    return datas

def ser_insert_billsell(_data: BillSells) -> str:
    bill_data = {
        "user_id": _data.user_id,
        "sell_date": _data.sell_date,
        "name": _data.name,
        "email": _data.email,
        "phone": _data.phone,
        "address": _data.address,
        "address_detail": _data.address_detail,
        "total_price": _data.total_price,
        "status": _data.status
    }

    result = billsell_collection.insert_one(bill_data)
    bill_id = str(result.inserted_id)

    if _data.sell_items:
        sell_items = _data.sell_items
        for item in sell_items:
            item.sell_id = bill_id 

        sellitem_collection.insert_many([item.dict(exclude={"id"}) for item in sell_items])

    return bill_id

def ser_update_billsell(_data: BillSells, billsell_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_billsell = billsell_collection.find_one({"_id": object_id})
    if not existing_billsell:
        raise HTTPException(status_code=404, detail="billsell not found")
    
    updated_billsell = billsell_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_billsell.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def ser_delete_billsell(billsell_id: str, billsell_collection: Collection):
    if not ObjectId.is_valid(billsell_id):
        raise HTTPException(status_code=400, detail="Invalid billsell ID")

    result = billsell_collection.delete_one({"_id": ObjectId(billsell_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="billsell not found")
    
    return {"message": "billsell deleted successfully"}
