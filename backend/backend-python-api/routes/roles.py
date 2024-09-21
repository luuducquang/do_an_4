from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Roles
from service.roles import delete_role, insert_role,update_role
from bson import ObjectId


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
def create_role(_data: Roles):
    _id = insert_role(_data, role_collection)
    return {"message": "Role created successfully", "_id": _id}

@router.put("/roles/update")
def update_role(_data: Roles):
    result = update_role(_data, role_collection)
    return result

@router.delete("/roles/delete/{role_id}")
def remove_role(role_id: str):
    response = delete_role(role_id, role_collection)
    return response


