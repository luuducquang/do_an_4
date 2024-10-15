from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import MenuItems
from config.database import database

menuitem_collection: Collection = database['MenuItems']

def ser_get_menuitem():
    datas = []
    for data in menuitem_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

def ser_insert_menuitem(_data: MenuItems) -> str:
    result = menuitem_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def ser_update_menuitem(_data: MenuItems, menuitem_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_menuitem = menuitem_collection.find_one({"_id": object_id})
    if not existing_menuitem:
        raise HTTPException(status_code=404, detail="menuitem not found")
    
    updated_menuitem = menuitem_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_menuitem.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def ser_delete_menuitem(menuitem_id: str, menuitem_collection: Collection):
    if not ObjectId.is_valid(menuitem_id):
        raise HTTPException(status_code=400, detail="Invalid menuitem ID")

    result = menuitem_collection.delete_one({"_id": ObjectId(menuitem_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="menuitem not found")
    
    return {"message": "menuitem deleted successfully"}
