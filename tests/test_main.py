from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_add():
    r = client.post("/add", json={"a": 2, "b": 3})
    assert r.json() == {"result": 5}


def test_subtract():
    r = client.post("/subtract", json={"a": 5, "b": 3})
    assert r.json() == {"result": 2}


def test_multiply():
    r = client.post("/multiply", json={"a": 4, "b": 3})
    assert r.json() == {"result": 12}


def test_divide():
    r = client.post("/divide", json={"a": 10, "b": 4})
    assert r.json() == {"result": 2.5}


def test_divide_by_zero():
    r = client.post("/divide", json={"a": 1, "b": 0})
    assert r.status_code == 400
