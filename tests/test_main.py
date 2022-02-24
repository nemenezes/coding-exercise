"""Test all API endpoints - run `python -m pytest`."""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/helloworld")
    assert response.status_code == 200
    msg = response.json().get("msg", "")
    assert msg == "Hello World"


def test_add_two_numbers():
    response = client.get("/add/?first=-4&second=67")
    assert response.status_code == 200
    result = response.json().get("sum", "")
    assert result == 63


def test_add_two_numbers_type_error():
    response = client.get("/add/?first=4.5&second=9")
    assert response.status_code == 422


def test_join_strings():
    response = client.get("/joinstrings/?first_str=pink&second_str=elephant")
    assert response.status_code == 200
    result = response.json().get("output", "")
    assert result == "pink-elephant"