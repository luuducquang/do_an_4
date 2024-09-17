from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.upload import router as upload_router
from routes.roles import router as roles_router
from routes.users import router as users_router

app = FastAPI()

app.include_router(upload_router)
app.include_router(roles_router)
app.include_router(users_router)

app.mount("/static", StaticFiles(directory="static"), name="static")