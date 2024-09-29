from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import FoodOrders
from service.foodorders import delete_foodorder, insert_foodorder, update_foodorder


router = APIRouter()

foodorder_collection: Collection = database['FoodOrders']

@router.get("/foodorders/get")
async def get_foodorder():
    datas = []
    for data in foodorder_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/foodorders/add")
async def create_foodorder(_data: FoodOrders):
    _id = insert_foodorder(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/foodorders/update")
def edit_foodorder(_data: FoodOrders):
    result = update_foodorder(_data, foodorder_collection)
    return result

@router.delete("/foodorders/delete/{foodorder_id}")
def remove_foodorder(foodorder_id: str):
    response = delete_foodorder(foodorder_id, foodorder_collection)
    return response