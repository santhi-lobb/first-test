from fastapi import FastAPI, HTTPException
from utils import get_data, find_employee_by_id, find_employee_by_name

app = FastAPI()

@app.get("/")
def get_employees():
    return get_data()


@app.get("/search")
def search_employees(name: str):
    return find_employee_by_name(name)


@app.get("/{employee_id}")
def get_employee(employee_id: int):
    employee = find_employee_by_id(employee_id)
    if employee:
        return employee
    raise HTTPException(status_code=404, detail="Employee not found")

