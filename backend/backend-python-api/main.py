from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.upload import router as upload_router
from routes.roles import router as roles_router
from routes.users import router as users_router
from routes.employeeTypes import router as employeeTypes_router
from routes.employees import router as employees_router
from routes.employeePayments import router as employeepayment_router
from routes.shifts import router as shift_router
from routes.bookings import router as booking_router
from routes.tableTypes import router as tableTypes_router
from routes.tables import router as tables_router
from routes.rentals import router as rentals_router
from routes.rentalItems import router as rentalItems_router
from routes.foodorders import router as foodOrders_routers
from routes.orderItems import router as orderItems_router
from routes.categoryMenuItems import router as categorys_router
from routes.menuItems import router as menuItems_router
from routes.timeSessions import router as timeSessions_router
from routes.pricingRules import router as pricingRules_router
from routes.manufactors import router as manufactors_router
from routes.categoryRentalItems import router as categoryrentalitems_router
from routes.suppliers import router as suppliers_router
from routes.importBills import router as importbills_router
from routes.importItems import router as importitems_router
from routes.news import router as news_router
from routes.login import router as login_router
from routes.tablemenuitems import router as table_menu_items_router
from routes.tablerentalitems import router as table_rental_items_router
from routes.carts import router as carts_router
from routes.banners import router as banners_router

from socketio_server import sio_app


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_router)
app.include_router(roles_router)
app.include_router(users_router)
app.include_router(employeeTypes_router)
app.include_router(employees_router)
app.include_router(employeepayment_router)
app.include_router(shift_router)
app.include_router(booking_router)
app.include_router(tableTypes_router)
app.include_router(tables_router)
app.include_router(rentals_router)
app.include_router(rentalItems_router)
app.include_router(foodOrders_routers)
app.include_router(orderItems_router)
app.include_router(categorys_router)
app.include_router(menuItems_router)
app.include_router(timeSessions_router)
app.include_router(pricingRules_router)
app.include_router(manufactors_router)
app.include_router(categoryrentalitems_router)
app.include_router(suppliers_router)
app.include_router(importbills_router)
app.include_router(importitems_router)
app.include_router(news_router)
app.include_router(login_router)
app.include_router(table_menu_items_router)
app.include_router(table_rental_items_router)
app.include_router(carts_router)
app.include_router(banners_router)


app.mount("/socket.io", sio_app)

app.mount("/static", StaticFiles(directory="static"), name="static")