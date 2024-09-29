from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import OrderItems
from service.orderItems import delete_orderitem, insert_orderitem, update_orderitem


router = APIRouter()

orderitem_collection: Collection = database['OrderItems']

@router.get("/orderitems/get")
async def get_orderitem():
    datas = []
    for data in orderitem_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/orderitems/add")
async def create_orderitem(_data: OrderItems):
    _id = insert_orderitem(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/orderitems/update")
def edit_orderitem(_data: OrderItems):
    result = update_orderitem(_data, orderitem_collection)
    return result

@router.delete("/orderitems/delete/{orderitem_id}")
def remove_orderitem(orderitem_id: str):
    response = delete_orderitem(orderitem_id, orderitem_collection)
    return response