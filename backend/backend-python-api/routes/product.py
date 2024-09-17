from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import ImageProducts
from service.product_service import insert_product    

router = APIRouter()

product_collection: Collection = database['AnhSanPham']

@router.get("/products")
async def get_products():
    datas = []
    for data in product_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

@router.post("/products/")
async def create_product(_data: ImageProducts):
    _id = insert_product(_data)
    return {"message": "Product created successfully", "_id": _id}



