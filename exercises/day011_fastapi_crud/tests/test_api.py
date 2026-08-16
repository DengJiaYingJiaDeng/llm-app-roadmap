from fastapi.testclient import TestClient

from app.db import get_db
from app.main import app

def fake_db():
    yield None

app.dependency_overrides[get_db] = fake_db

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status" : "ok"
    }

def test_create_document_empty_title():
    response = client.post(
        "/documents",
        json={
            "user_id": 1,
            "title": "",
            "content": "test",
        },
    )

    assert response.status_code == 422


def test_create_document_invalid_user_id():
    response = client.post(
        "/documents",
        json={
            "user_id": 0,
            "title": "test",
            "content": "test",
        },
    )

    assert response.status_code == 422


def test_create_document_wrong_user_id_type():
    response = client.post(
        "/documents",
        json={
            "user_id": "abc",
            "title": "test",
            "content": "test",
        },
    )

    assert response.status_code == 422