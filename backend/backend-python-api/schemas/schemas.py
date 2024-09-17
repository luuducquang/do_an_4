from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Roles(BaseModel):
    role_name: str
    role_description: str

class Users(BaseModel):
    username: str
    password: str
    email: str
    phone: Optional[str]
    address: Optional[str]
    loyalty_points: Optional[int]
    role_name: str

class EmployeeTypes(BaseModel):
    employee_type_id: int
    employee_type_name: str

class Employees(BaseModel):
    employee_id: int
    employee_type_id: str
    user_id: int
    hourly_rate: Optional[float]
    monthly_salary: Optional[float]

class Shifts(BaseModel):
    shift_id: int
    employee_id: int
    shift_date: datetime
    start_time: datetime
    end_time: datetime
    hours_worked: Optional[float]

class EmployeePayments(BaseModel):
    payment_id: int
    employee_id: int
    pay_period_start: datetime
    pay_period_end: datetime
    total_hours: Optional[float]
    total_payment: Optional[float]

class Bookings(BaseModel):
    booking_id: int
    user_id: int
    table_id: int
    booking_date: datetime
    start_time: datetime
    end_time: datetime
    status: Optional[bool]

class TableTypes(BaseModel):
    table_type_id: int
    table_type_name: str

class Tables(BaseModel):
    table_id: int
    table_number: int
    type: str
    status: Optional[bool]

class Rentals(BaseModel):
    rental_id: int
    user_id: int
    item_id: int
    rental_date: Optional[datetime]
    return_date: Optional[datetime]
    quantity: int
    price: Optional[float]
    status: Optional[bool]

class RentalItems (BaseModel):
    item_id: int
    item_name: str
    rental_price_day: int
    rental_price_hours: int
    quantity_available: int

class FoodOrders(BaseModel):
    order_id: int
    user_id: int
    order_date: str
    status: str
    total_price: Optional[float]

class OrderItems(BaseModel):
    order_item_id: int
    order_id: int
    item_id: int
    quantity: int
    price: Optional[float]

class Categorys(BaseModel):
    category_id: int
    category_name: str

class MenuItems(BaseModel):
    item_id: int
    name: str
    stock_quantity: int
    price: Optional[float]
    category_id: Optional[int]

class TimeSessions(BaseModel):
    session_id: int
    table_id: int
    start_time: datetime
    end_time: datetime
    price: Optional[float]


class PricingRules(BaseModel):
    rate_id: int
    type_table_id: int
    rate_per_hour: int
    rate_per_minute: int


