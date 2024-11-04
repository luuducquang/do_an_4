from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.schemas import RentalItems, Searchs
from config.database import database

rentalitem_collection: Collection = database['RentalItems']
categoryrentalitem_collection: Collection = database['CategoryRentalItems']
manufactor_collection: Collection = database['Manufactors']

def ser_get_rentalitem():
    datas = []
    for data in rentalitem_collection.find():
        data["_id"] = str(data["_id"])
        datas.append(data)
    return datas

def ser_getbyid_rentalitem(_data: RentalItems) -> str:
    result = rentalitem_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def ser_getbyid_rentalitem(rentalitem_id:str):
    if not ObjectId.is_valid(rentalitem_id):
            raise HTTPException(status_code=400, detail="Invalid ID format")

    rentalitem_data = rentalitem_collection.find_one({"_id": ObjectId(rentalitem_id)})

    if rentalitem_data is None:
        raise HTTPException(status_code=404, detail="rentalitem not found")

    rentalitem_data["_id"] = str(rentalitem_data["_id"])
    categoryrentalitem_data = categoryrentalitem_collection.find_one({"_id": ObjectId(rentalitem_data["category_id"])})
    if categoryrentalitem_data:
        categoryrentalitem_data["_id"] = str(categoryrentalitem_data["_id"])  
        rentalitem_data["categoryrentalitem"] = categoryrentalitem_data  
    else:
        rentalitem_data["categoryrentalitem"] = None  

    manufactor_data = manufactor_collection.find_one({"_id": ObjectId(rentalitem_data["manufactor_id"])})
    if manufactor_data:
        manufactor_data["_id"] = str(manufactor_data["_id"])  
        rentalitem_data["manufactor"] = manufactor_data  
    else:
        rentalitem_data["manufactor"] = None  
    
    return rentalitem_data

def ser_search_rentalitem(_data:Searchs):
    if _data.page <= 0 or _data.pageSize <= 0:
        raise HTTPException(status_code=400, detail="Page and pageSize must be greater than 0")
    
    skip = (_data.page - 1) * _data.pageSize

    query = {}
    if _data.search_term:
        query["$or"] = [
            {"item_name": {"$regex": _data.search_term, "$options": "i"}},
            {"price": {"$regex": _data.search_term, "$options": "i"}},
            {"price_reduction": {"$regex": _data.search_term, "$options": "i"}},
            {"rental_price_day": {"$regex": _data.search_term, "$options": "i"}},
            {"rental_price_hours": {"$regex": _data.search_term, "$options": "i"}},
            {"quantity_available": {"$regex": _data.search_term, "$options": "i"}},
            {"view": {"$regex": _data.search_term, "$options": "i"}},
            {"origin": {"$regex": _data.search_term, "$options": "i"}},
            {"description": {"$regex": _data.search_term, "$options": "i"}},
            {"description_detail": {"$regex": _data.search_term, "$options": "i"}},
        ]

    total_items = rentalitem_collection.count_documents(query)

    rentalitems = rentalitem_collection.find(query).skip(skip).limit(_data.pageSize)

    data = []
    for rentalitem in rentalitems:
        rentalitem["_id"] = str(rentalitem["_id"])
        categoryrentalitem_data = categoryrentalitem_collection.find_one({"_id": ObjectId(rentalitem["category_id"])})
        if categoryrentalitem_data:
            categoryrentalitem_data["_id"] = str(categoryrentalitem_data["_id"])  
            rentalitem["categoryrentalitem"] = categoryrentalitem_data  
        else:
            rentalitem["categoryrentalitem"] = None  

        manufactor_data = manufactor_collection.find_one({"_id": ObjectId(rentalitem["manufactor_id"])})
        if manufactor_data:
            manufactor_data["_id"] = str(manufactor_data["_id"])  
            rentalitem["manufactor"] = manufactor_data  
        else:
            rentalitem["manufactor"] = None  

        data.append(rentalitem)

    return {
        "page":_data.page,
        "pageSize":_data.pageSize,
        "totalItems": total_items,
        "data": data,
    }

def ser_insert_rentalitem(_data: RentalItems) -> str:
    result = rentalitem_collection.insert_one(_data.dict(exclude={"id"}))
    return str(result.inserted_id)

def ser_update_rentalitem(_data: RentalItems, rentalitem_collection: Collection):
    if not _data.id:
        raise HTTPException(status_code=400, detail="ID is required for update")

    try:
        object_id = ObjectId(_data.id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    existing_rentalitem = rentalitem_collection.find_one({"_id": object_id})
    if not existing_rentalitem:
        raise HTTPException(status_code=404, detail="rentalitem not found")
    
    updated_rentalitem = rentalitem_collection.update_one(
    {"_id": ObjectId(_data.id)},  
    {"$set": _data.dict(exclude={"id"})} 
)
    
    if updated_rentalitem.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed")

    return {"message": "updated successfully"}


def ser_delete_rentalitem(rentalitem_id: str, rentalitem_collection: Collection):
    if not ObjectId.is_valid(rentalitem_id):
        raise HTTPException(status_code=400, detail="Invalid rentalitem ID")

    result = rentalitem_collection.delete_one({"_id": ObjectId(rentalitem_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="rentalitem not found")
    
    return {"message": "rentalitem deleted successfully"}
