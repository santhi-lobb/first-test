"""FastAPI application to manage employee data."""
from fastapi import FastAPI, HTTPException
from utils import get_data, filter_employees

app = FastAPI()

@app.get("/")
def get_employees():
    """Return a list of all employees."""
    return get_data()


@app.get("/filter", status_code=200)
def filter_emp(name: str | None = None, email: str | None = None, phone: str | None = None):
    """Filters data based on the parameters"""
    try:
        filtered_data = filter_employees({
            "name": name, 
            "email": email,
            "phone": phone
        })
    except Exception:
        raise HTTPException(500, "Internal Server Error")
    if len(filtered_data) == 0:
        raise HTTPException(404, "No employees found")
    return filtered_data


# @app.get("/{employee_id}")
# def get_employee(employee_id: int):
#     """Return an employee by ID."""
#     employee = find_employee_by_id(employee_id)
#     if employee:
#         return employee
#     raise HTTPException(status_code=404, detail="Employee not found")
