from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Employees
from service.employees import delete_employee, insert_employee, update_employee


router = APIRouter()

employee_collection: Collection = database['Employees']

@router.get("/employees/get")
async def get_employee():
    datas = []
    for data in employee_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/employees/add")
async def create_employee(_data: Employees):
    _id = insert_employee(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/employees/update")
def edit_employee(_data: Employees):
    result = update_employee(_data, employee_collection)
    return result

@router.delete("/employees/delete/{employee_id}")
def remove_employee(employee_id: str):
    response = delete_employee(employee_id, employee_collection)
    return response