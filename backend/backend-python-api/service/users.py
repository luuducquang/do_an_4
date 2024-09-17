from pymongo.collection import Collection
from schemas.schemas import Users
from config.database import database

user_collection: Collection = database['Users']

def insert_user(user_data: Users) -> str:
    dict = user_data.dict()
    result = user_collection.insert_one(dict)
    return str(result.inserted_id)