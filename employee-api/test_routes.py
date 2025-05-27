import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_employee_by_valid_id():
    response = client.get('/employees/1')
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Robin Lam",
        "phone": "9015662787",
        "email": "robinlam@gmail.com",
        "age": 44,
        "gender": "male"
    }


def test_get_nonexistant_employee():
    response = client.get("/employees/123")
    assert response.status_code == 404
    assert response.json() == {"detail": "Employee not found"}    


def test_get_employee_invalid_id():
    response = client.get("/employees/abc")
    assert response.status_code == 400
    assert response.json() == {"detail": "ID should be numeric"}


def test_get_employee_500_error(mocker):
    mocker.patch(
        "employee_routes.find_employee_by_id",
        side_effect=Exception("error")
    )
    response = client.get("/employees/1")
    assert response.status_code == 500
    

def test_get_all_employees():
    response = client.get("/employees/")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        "name=saul",
        "email=ram@gmailcom",
        "phone=1234",
        "name=saul&phone=89899983",
        "name=tony&email=tony&phone=9"
    ]
)
def test_get_all_employees_valid_query(params):
    response = client.get(f"/employees?{params}")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        "invalid=900",
        "name=ram&number=23",
        "names=ram"
    ]
)
def test_get_all_employees_invalid_query(params):
    response = client.get(f"/employees?{params}")
    assert response.status_code == 400


def test_get_all_employees_500_error(mocker):
    mocker.patch("employee_routes.filter_employees",
                 side_effect=FileNotFoundError("json file not found"))
    response = client.get(f"/employees")
    assert response.status_code == 500

