from fastapi import FastAPI
from employee_routes import employee_router

app = FastAPI()

app.include_router(employee_router)
