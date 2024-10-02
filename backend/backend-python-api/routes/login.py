import jwt

from fastapi import APIRouter, Depends, HTTPException
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import LoginRequest
from typing import Union, Any
from datetime import datetime, timedelta


router = APIRouter()

user_collection: Collection = database['Users']

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

@router.post("/login")
def login(request_data: LoginRequest):
    user = user_collection.find_one({"username": request_data.username, "password": request_data.password})
    
    if user:
        token = generate_token(request_data.username)
        return {"message": "Login successful", "user": {"username": user["username"]},"token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    

def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt