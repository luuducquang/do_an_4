from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Users, Roles
from service.users import insert_user


router = APIRouter()

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