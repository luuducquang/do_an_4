from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import MenuItems
from service.menuItems import ser_get_menuitem,ser_delete_menuitem, ser_insert_menuitem, ser_update_menuitem


router = APIRouter()

menuitem_collection: Collection = database['MenuItems']

@router.get("/menuitems/get")
async def get_menuitem():
    return ser_get_menuitem()

@router.post("/menuitems/add")
async def create_menuitem(_data: MenuItems):
    _id = ser_insert_menuitem(_data)
    return {"message": "Created successfully", "_id": _id}

@router.put("/menuitems/update")
def edit_menuitem(_data: MenuItems):
    result = ser_update_menuitem(_data, menuitem_collection)
    return result

@router.delete("/menuitems/delete/{menuitem_id}")
def remove_menuitem(menuitem_id: str):
    response = ser_delete_menuitem(menuitem_id, menuitem_collection)
    return response