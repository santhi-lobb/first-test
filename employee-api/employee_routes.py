from fastapi import Request, HTTPException, APIRouter
from employee_utils import filter_employees, find_employee_by_id

employee_router = APIRouter(
    prefix="/employees"
)


@employee_router.get("/")
def get_employees(request: Request):
    """Return a list of all employees with optional filters."""
    params = request.query_params
    valid_params = {"name", "email", "phone"}
    name = params.get("name")
    email = params.get("email")
    phone = params.get("phone")
    if set(params.keys()) - valid_params:
        raise HTTPException(400, "Invalid parameter")
    
    try:
        filtered_data = filter_employees({
            "name": name,
            "email": email,
            "phone": phone
        })
    except:
        raise HTTPException(500, "Internal Server Error")
    return filtered_data


@employee_router.get('/{emp_id}')
def get_employee(emp_id: str):
    """Return a employee with employee id"""
    try:
        employee = find_employee_by_id(emp_id)
        return employee
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(500, str(e))

