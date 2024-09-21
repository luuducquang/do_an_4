from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

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

class EmployeeTypes(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    employee_type_name: str

class Employees(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    employee_type_id: str
    user_id: int
    hourly_rate: Optional[float]
    monthly_salary: Optional[float]

class Shifts(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    employee_id: int
    shift_date: datetime
    start_time: datetime
    end_time: datetime
    hours_worked: Optional[float]

class EmployeePayments(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    employee_id: int
    pay_period_start: datetime
    pay_period_end: datetime
    total_hours: Optional[float]
    total_payment: Optional[float]

class Bookings(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: int
    table_id: int
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
    type: str
    status: Optional[bool]

class Rentals(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: int
    item_id: int
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
    user_id: int
    order_date: str
    status: str
    total_price: Optional[float]

class OrderItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    order_id: int
    item_id: int
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
    category_id: Optional[int]

class TimeSessions(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    table_id: int
    start_time: datetime
    end_time: datetime
    price: Optional[float]


class PricingRules(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    type_table_id: int
    rate_per_hour: int
    rate_per_minute: int


