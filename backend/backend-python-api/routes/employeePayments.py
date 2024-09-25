from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import EmployeePayments
from service.employeePayments import delete_employeepayment, insert_employeepayment, update_employeepayment


router = APIRouter()

employeepayment_collection: Collection = database['EmployeePayments']

@router.get("/employeepayments/get")
async def get_employeepayment():
    datas = []
    for data in employeepayment_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/employeepayments/add")
async def create_employeepayment(_data: EmployeePayments):
    _id = insert_employeepayment(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/employeepayments/update")
def edit_employee(_data: EmployeePayments):
    result = update_employeepayment(_data, employeepayment_collection)
    return result

@router.delete("/employeepayments/delete/{employeepayment_id}")
def remove_employee(employeepayment_id: str):
    response = delete_employeepayment(employeepayment_id, employeepayment_collection)
    return response