from fastapi import APIRouter, HTTPException
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

@router.get("/roles/get/{role_id}")
async def get_role_by_id(role_id: str):
    if not ObjectId.is_valid(role_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    role = role_collection.find_one({"_id": ObjectId(role_id)})

    if role is None:
        raise HTTPException(status_code=404, detail="role not found")

    role["_id"] = str(role["_id"])
    return role

@router.post("/roles/add")
def create_role(_data: Roles):
    _id = insert_role(_data, role_collection)
    return {"message": "Role created successfully", "_id": _id}

@router.put("/roles/update")
def edit_role(_data: Roles):
    result = update_role(_data, role_collection)
    return result

@router.delete("/roles/delete/{role_id}")
def remove_role(role_id: str):
    response = delete_role(role_id, role_collection)
    return response


