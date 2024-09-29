from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import TimeSessions
from service.timeSessions import delete_timesession, insert_timesession, update_timesession


router = APIRouter()

timesession_collection: Collection = database['TimeSessions']

@router.get("/timesessions/get")
async def get_timesession():
    datas = []
    for data in timesession_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/timesessions/add")
async def create_timesession(_data: TimeSessions):
    _id = insert_timesession(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/timesessions/update")
def edit_timesession(_data: TimeSessions):
    result = update_timesession(_data, timesession_collection)
    return result

@router.delete("/timesessions/delete/{timesession_id}")
def remove_timesession(timesession_id: str):
    response = delete_timesession(timesession_id, timesession_collection)
    return response