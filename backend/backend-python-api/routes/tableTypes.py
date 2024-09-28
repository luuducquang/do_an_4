from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import TableTypes
from service.tableTypes import delete_tabletype, insert_tabletype, update_tabletype


router = APIRouter()

tabletype_collection: Collection = database['TableTypes']

@router.get("/tabletypes/get")
async def get_tabletype():
    datas = []
    for data in tabletype_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/tabletypes/add")
async def create_tabletype(_data: TableTypes):
    _id = insert_tabletype(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/tabletypes/update")
def edit_tabletype(_data: TableTypes):
    result = update_tabletype(_data, tabletype_collection)
    return result

@router.delete("/tabletypes/delete/{tabletype_id}")
def remove_tabletype(tabletype_id: str):
    response = delete_tabletype(tabletype_id, tabletype_collection)
    return response