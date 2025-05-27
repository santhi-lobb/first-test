from fastapi import HTTPException
import json


def get_data():
    """Return a list of dictionaries from the JSON file."""
    with open('employees.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def find_employee_by_id(employee_id):
    """Return an employee dictionary by ID."""
    if not employee_id.isdigit():
        raise HTTPException(400, "ID should be numeric")
    employees = get_data()
    for employee in employees:
        if employee['id'] == int(employee_id):
            return employee
    raise HTTPException(404, "Employee not found")


def filter_employees(filter_data):
    """Return employees whose fields contains the value"""
    employees = get_data()
    for field, value in filter_data.items():
        if value is not None:
            employees = [emp for emp in employees if value.lower() in emp[field].lower()]
    return employees
