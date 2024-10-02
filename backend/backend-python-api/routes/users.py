from fastapi import APIRouter, Depends
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Users
from service.users import delete_user, insert_user, update_user
from sercurity import validate_token


router = APIRouter(dependencies=[Depends(validate_token)])

user_collection: Collection = database['Users']

@router.get("/users/get")
async def get_users():
    datas = []
    for data in user_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/users/add")
async def create_user(_data: Users):
    _id = insert_user(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/users/update")
def edit_user(_data: Users):
    result = update_user(_data, user_collection)
    return result

@router.delete("/users/delete/{user_id}")
def remove_user(user_id: str):
    response = delete_user(user_id, user_collection)
    return response