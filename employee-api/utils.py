"""Utility functions for employee data handling."""
import json


def get_data():
    """Return a list of dictionaries from the JSON file."""
    with open('employees.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def find_employee_by_id(employee_id):
    """Return an employee dictionary by ID."""
    employees = get_data()
    for employee in employees:
        if employee['id'] == employee_id:
            return employee
    return None


def filter_employees(filter_data):
    """Return employees whose fields contains the value"""
    employees = get_data()
    for field, value in filter_data.items():
        if value is not None:
            employees = [emp for emp in employees if value.lower() in emp[field].lower()]
    return employees
