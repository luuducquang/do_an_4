from typing import Optional
from bson import ObjectId,errors
from fastapi import APIRouter, Body, HTTPException
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Employees
from service.employees import delete_employee, insert_employee, update_employee


router = APIRouter()

employee_collection: Collection = database['Employees']
user_collection: Collection = database['Users']

@router.get("/employees/get")
async def get_employee():
    datas = []
    for employee in employee_collection.find():
        try:
            user_id = ObjectId(employee["user_id"])
        except (errors.InvalidId, KeyError):
            user_data = None
        else:
            user_data = user_collection.find_one({"_id": user_id})
        employee["_id"] = str(employee["_id"])
        if user_data:
            user_data["_id"] = str(user_data["_id"])
            employee["user_info"] = {
                "username": user_data["username"],
                "fullname": user_data.get("fullname", ""),
                "email": user_data["email"],
                "phone": user_data.get("phone", ""),
                "address": user_data.get("address", ""),
                "avatar": user_data.get("avatar", ""),
                "loyalty_points": user_data.get("loyalty_points", 0),
                "role_name": user_data["role_name"]
            }
        else:
            employee["user_info"] = {}
        datas.append(employee)
    return datas


@router.get("/employees/get/{employee_id}")
async def get_employee_by_id(employee_id: str):
    if not ObjectId.is_valid(employee_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    employee = employee_collection.find_one({"_id": ObjectId(employee_id)})

    if employee is None:
        raise HTTPException(status_code=404, detail="employee not found")
    user_id = ObjectId(employee["user_id"])
    user_data = user_collection.find_one({"_id": user_id})
    employee["_id"] = str(employee["_id"])
    if user_data:
            user_data["_id"] = str(user_data["_id"])
            employee["user_info"] = {
                "username": user_data["username"],
                "fullname": user_data.get("fullname", ""),
                "email": user_data["email"],
                "phone": user_data.get("phone", ""),
                "address": user_data.get("address", ""),
                "avatar": user_data.get("avatar", ""),
                "loyalty_points": user_data.get("loyalty_points", 0),
                "role_name": user_data["role_name"]
            }
    else:
        employee["user_info"] = {}
    return employee

@router.post("/employees/search")
async def search_employee(
    page: int = Body(...),
    pageSize: int = Body(...),
    search_term: Optional[str] = Body(None)  
):
    if page <= 0 or pageSize <= 0:
        raise HTTPException(status_code=400, detail="Page and pageSize must be greater than 0")
    
    skip = (page - 1) * pageSize

    user_query = {}
    if search_term:
        user_query["$or"] = [
            {"username": {"$regex": search_term, "$options": "i"}},
            {"fullname": {"$regex": search_term, "$options": "i"}},
            {"email": {"$regex": search_term, "$options": "i"}},
            {"phone": {"$regex": search_term, "$options": "i"}}
        ]

    users = user_collection.find(user_query)
    user_ids = [str(user["_id"]) for user in users]

    if not user_ids:
        return {
            "page": page,
            "pageSize": pageSize,
            "totalItems": 0,
            "data": []
        }

    employee_query = {"user_id": {"$in": user_ids}}

    total_items = employee_collection.count_documents(employee_query)

    employees = employee_collection.find(employee_query).skip(skip).limit(pageSize)

    data = []
    for employee in employees:
        employee["_id"] = str(employee["_id"])
        user = user_collection.find_one({"_id": ObjectId(employee["user_id"])})
        if user:
            employee["user_info"] = {
                "username": user["username"],
                "fullname": user.get("fullname", ""),
                "email": user["email"],
                "phone": user.get("phone", ""),
                "address": user.get("address", ""),
                "avatar": user.get("avatar", ""),
                "loyalty_points": user.get("loyalty_points", 0),
                "role_name": user["role_name"]
            }
        data.append(employee)

    return {
        "page": page,
        "pageSize": pageSize,
        "totalItems": total_items,
        "data": data,
    }


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