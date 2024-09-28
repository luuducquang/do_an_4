from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import Tables
from service.tables import delete_table, insert_table, update_table


router = APIRouter()

table_collection: Collection = database['Tables']

@router.get("/tables/get")
async def get_table():
    datas = []
    for data in table_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/tables/add")
async def create_table(_data: Tables):
    _id = insert_table(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/tables/update")
def edit_table(_data: Tables):
    result = update_table(_data, table_collection)
    return result

@router.delete("/tables/delete/{table_id}")
def remove_table(table_id: str):
    response = delete_table(table_id, table_collection)
    return response