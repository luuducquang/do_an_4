from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import PricingRules
from service.pricingRules import delete_pricingrule, insert_pricingrule, update_pricingrule


router = APIRouter()

pricingrule_collection: Collection = database['PricingRules']

@router.get("/pricingrules/get")
async def get_pricingrule():
    datas = []
    for data in pricingrule_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/pricingrules/add")
async def create_pricingrule(_data: PricingRules):
    _id = insert_pricingrule(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/pricingrules/update")
def edit_pricingrule(_data: PricingRules):
    result = update_pricingrule(_data, pricingrule_collection)
    return result

@router.delete("/pricingrules/delete/{pricingrule_id}")
def remove_pricingrule(pricingrule_id: str):
    response = delete_pricingrule(pricingrule_id, pricingrule_collection)
    return response