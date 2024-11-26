from fastapi import Body
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Searchs(BaseModel):
    page: int = Body(...),
    pageSize: int = Body(...),
    search_term: Optional[str] = Body(None)
    category_name:Optional[str] = Body(None)

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
    fullname: Optional[str] = None
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    avatar: Optional[str] = None
    loyalty_points: Optional[int] = 0
    role_name: str

class News(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: str
    title: str
    content: str
    image: str
    view: Optional[int] = 0
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
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class TableMenuItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    table_id:str
    item_id: str
    quantity: int
    unit_price: int
    total_price: int

class TableRentalItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    table_id:str
    item_id: str
    quantity: int
    unit_price: int
    total_price: int

class Suppliers(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    name: str
    phone:str
    address: str

class Manufactors(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    name: str
    phone:str
    address: str

class CategoryRentalItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    category_name: str

class Rentals(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: str
    item_id: str
    rental_date: Optional[datetime]
    return_date: Optional[datetime]
    quantity: int
    price: Optional[int]
    status: Optional[bool]

class RentalItems (BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    manufactor_id: str
    category_id: str
    item_name: str
    image: str
    price: int
    price_reduction: int
    rental_price_day: int
    rental_price_hours: int
    quantity_available: int = Field(default=0)
    view: int = Field(default=0)
    sales: int = Field(default=0)
    origin: str
    description: str
    description_detail: str

class FoodOrders(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: str
    order_date: datetime
    status: str
    total_price: Optional[int]

class OrderItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    order_id: str
    item_id: str
    quantity: int
    unit_price: int
    total_price: int

class CategoryMenuItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    category_name: str

class MenuItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    name: str
    image:str
    stock_quantity: int
    price: Optional[int]
    category_id: Optional[str]

class TimeSessions(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    table_id: str
    start_time: datetime
    end_time: datetime
    price: Optional[int]


class PricingRules(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    type_table_id: str
    rate_per_hour: int
    rate_per_minute: int

class ImportBills(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id: str
    import_date: datetime
    total_price: int

class ImportItems(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    import_id: str
    item_id: str
    quantity: int
    unit_price: int
    total_price: int

class Carts(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    user_id:str
    item_id:str
    quantity:int
    status:bool
    
class Banners(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  
    description:str
    image:str


