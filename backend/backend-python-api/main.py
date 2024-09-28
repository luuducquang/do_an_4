from fastapi import FastAPI
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

app = FastAPI()

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

app.mount("/static", StaticFiles(directory="static"), name="static")