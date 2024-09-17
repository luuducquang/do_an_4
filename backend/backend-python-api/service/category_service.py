from pymongo.collection import Collection
from schemas.schemas import Categorys
from config.database import database

category_collection: Collection = database['Categorys']

def insert_category(product_data: Categorys) -> str:
    product_dict = product_data.dict()
    result = category_collection.insert_one(product_dict)
    return str(result.inserted_id)