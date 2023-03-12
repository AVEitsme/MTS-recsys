from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_select_all_users():
    response = client.get("/select_all_users", params={"limit": 10})
    assert response.status_code == 200

def test_select_users_by_ids():
    response = client.post("/select_users_by_ids", json=[1, 2, 3])
    assert response.status_code == 200
    response = client.post("/select_users_by_ids", json=[1, 2, ""])
    assert response.status_code == 422

def test_insert_users():
    response = client.post("/insert_users", json=[{"user_id": 1, "user_age": "18_24", "user_sex": True}])
    assert response.status_code == 500
    response = client.post("/insert_users", json=[{"user_id": "", "user_age": "18_24", "user_sex": True}])
    assert response.status_code == 422

def test_update_users():
    response = client.put("/update_users", json=[{"user_id": 1, "user_age": "45_54", "user_sex": True}])
    assert response.status_code == 200
    response = client.put("/update_users", json=[{"user_id": "", "user_age": "45_54", "user_sex": True}])
    assert response.status_code == 422