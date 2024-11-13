from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Carts
from service.carts import ser_get_cart,ser_delete_cart, ser_insert_cart, ser_update_cart,ser_get_cart_by_user_id


router = APIRouter()

cart_collection: Collection = database['Carts']

@router.get("/carts/get")
async def get_cart():
    return ser_get_cart()

@router.get("/carts/get/{user_id}")
async def get_cart_by_user_id(user_id: str):
    return ser_get_cart_by_user_id(user_id)

@router.post("/carts/add")
async def create_cart(_data: Carts):
    _id = ser_insert_cart(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/carts/update")
def edit_cart(_data: Carts):
    result = ser_update_cart(_data, cart_collection)
    return result

@router.delete("/carts/delete/{cart_id}")
def remove_cart(cart_id: str):
    response = ser_delete_cart(cart_id, cart_collection)
    return response