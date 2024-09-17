from pymongo.collection import Collection
from schemas.schemas import Roles
from config.database import database

role_collection: Collection = database['Roles']

def insert_role(role_data: Roles) -> str:
    dict = role_data.dict()
    result = role_collection.insert_one(dict)
    return str(result.inserted_id)