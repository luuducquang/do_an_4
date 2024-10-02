from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class LoginRequest(BaseModel):
    username: str
    password: str

class Roles(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    role_name: str
    role_description: Optional[str] = None

class Users(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    username: str
    password: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    loyalty_points: Optional[int] = 0
    role_name: str

class News(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: str
    title: str
    content: str
    image: str
    view: int
    status: bool

class EmployeeTypes(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    employee_type_name: str

class Employees(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    employee_type_id: str
    user_id: str
    hourly_rate: Optional[float]
    monthly_salary: Optional[float]

class Shifts(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    employee_id: str
    shift_date: datetime
    start_time: datetime
    end_time: datetime
    hours_worked: Optional[float]

class EmployeePayments(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    employee_id: str
    pay_period_start: datetime
    pay_period_end: datetime
    total_hours: Optional[float]
    total_payment: Optional[float]

class Bookings(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: str
    table_id: str
    booking_date: datetime
    start_time: datetime
    end_time: datetime
    status: Optional[bool]

class TableTypes(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    table_type_name: str

class Tables(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    table_number: int
    table_type_id: str
    status: Optional[bool]

class Rentals(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: str
    item_id: str
    rental_date: Optional[datetime]
    return_date: Optional[datetime]
    quantity: int
    price: Optional[float]
    status: Optional[bool]

class RentalItems (BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    item_name: str
    rental_price_day: int
    rental_price_hours: int
    quantity_available: int

class FoodOrders(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: str
    order_date: datetime
    status: str
    total_price: Optional[float]

class OrderItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    order_id: str
    item_id: str
    quantity: int
    price: Optional[float]

class Categorys(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    category_name: str

class MenuItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    name: str
    stock_quantity: int
    price: Optional[float]
    category_id: Optional[str]

class TimeSessions(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    table_id: str
    start_time: datetime
    end_time: datetime
    price: Optional[float]


class PricingRules(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    type_table_id: str
    rate_per_hour: int
    rate_per_minute: int


