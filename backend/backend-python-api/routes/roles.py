from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Roles
from service.roles import insert_role


router = APIRouter()

role_collection: Collection = database['Roles']

@router.get("/roles/get")
async def get_roles():
    datas = []
    for data in role_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/roles/add")
async def create_role(_data: Roles):
    _id = insert_role(_data)
    return {"message": "Created successfully", "_id": _id}