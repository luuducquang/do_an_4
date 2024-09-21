from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import EmployeeTypes
from service.employeeTypes import delete_employeetype, insert_employeetype, update_employeetype


router = APIRouter()

employeetype_collection: Collection = database['EmployeeTypes']

@router.get("/employeetypes/get")
async def get_employeetype():
    datas = []
    for data in employeetype_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/employeetypes/add")
async def create_employeetype(_data: EmployeeTypes):
    _id = insert_employeetype(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/employeetypes/update")
def edit_employeetype(_data: EmployeeTypes):
    result = update_employeetype(_data, employeetype_collection)
    return result

@router.delete("/employeetypes/delete/{employeetype_id}")
def remove_employeetype(employeetype_id: str):
    response = delete_employeetype(employeetype_id, employeetype_collection)
    return response