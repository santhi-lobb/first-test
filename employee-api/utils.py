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


def find_employee_by_name(name):
    """Return employees matching the name."""
    employees = get_data()
    return [employee for employee in employees if name in employee['name']]
