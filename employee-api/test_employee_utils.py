import pytest
import employee_utils
from fastapi import HTTPException

fake_data = [
    {"id": 1, "name": "Tony"},
    {"id": 2, "name": "John"}
]


@pytest.fixture(autouse=True)
def mock_employee_data(mocker, request):
    if "noautofixture" in request.keywords:
        return
    mocker.patch("employee_utils.get_data", return_value=fake_data)
    return fake_data


@pytest.mark.noautofixture
def test_get_data(mocker):
    mock_open = mocker.patch("builtins.open")
    mock_json = mocker.patch("json.load")
    mock_json.return_value = fake_data
    result = employee_utils.get_data()
    assert result == fake_data
    mock_json.assert_called_once()
    mock_open.assert_called_once()


def test_find_employee_by_id_success():
    result = employee_utils.find_employee_by_id("2")
    assert result == {"id": 2, "name": "John"}


def test_find_employee_by_id_non_numeric():
    with pytest.raises(HTTPException, match="400"):
        employee_utils.find_employee_by_id("i2")


def test_find_employee_by_id_not_found():
    with pytest.raises(HTTPException, match="404"):
        employee_utils.find_employee_by_id("3")


@pytest.mark.parametrize(
    "filter_data",
    [
        ({"name": "John"}),
        {"name": "J"},
        {"name": "oh"},
        {"name": "john"}
    ]
)
def test_filter_employees_get_john(filter_data):
    result = employee_utils.filter_employees(filter_data)
    assert result == [{"id": 2, "name": "John"}]


@pytest.mark.parametrize(
    "filter_data",
    [
        {"name": "o"},
        {"name": ""}
    ]
)
def test_filter_employees_get_both(filter_data):
    result = employee_utils.filter_employees(filter_data)
    assert result == [
        {"id": 1, "name": "Tony"},
        {"id": 2, "name": "John"}
    ]


@pytest.mark.parametrize(
    "filter_data",
    [
        {"name": "chris"},
        {"name": "Jn"},
    ]
)
def test_filter_employees_get_empty(filter_data):
    result = employee_utils.filter_employees(filter_data)
    assert result == []
