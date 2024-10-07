from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import ImportItems
from service.importItems import delete_importitem, insert_importitem, update_importitem


router = APIRouter()

importitem_collection: Collection = database['ImportItems']

@router.get("/importitems/get")
async def get_importitem():
    datas = []
    for data in importitem_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/importitems/add")
async def create_importitem(_data: ImportItems):
    _id = insert_importitem(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/importitems/update")
def edit_importitem(_data: ImportItems):
    result = update_importitem(_data, importitem_collection)
    return result

@router.delete("/importitems/delete/{importitem_id}")
def remove_importitem(importitem_id: str):
    response = delete_importitem(importitem_id, importitem_collection)
    return response