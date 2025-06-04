from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_classes():
    res = client.get("/classes")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_book_class():
    res = client.post("/book", json={
        "class_id": 1,
        "client_name": "Raj",
        "client_email": "raj@example.com"
    })
    assert res.status_code == 200
    assert res.json()["client_name"] == "Raj"

def test_get_bookings():
    res = client.get("/bookings?email=raj@example.com")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
