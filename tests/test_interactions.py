from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_select_all_interactions():
    response = client.get("/select_all_interactions", params={"limit": 10})
    assert response.status_code == 200

def test_insert_interactions():
    response = client.post(
        "/insert_interactions", 
        json=[
            {
                "user_id": 126706, "book_id": 14433, "progress": 80, "rating": 5, "start_date": "2018-01-01T00:00:00", "used_to_train": True
            }
        ]
    )
    assert response.status_code == 500
    response = client.post(
        "/insert_interactions", 
        json=[
            {
                "user_id": "", "book_id": 14433, "progress": 80, "rating": 5, "start_date": "2018-01-01T00:00:00", "used_to_train": True
            }
        ]
    )
    assert response.status_code == 422

def test_update_interactions():
    response = client.put(
        "/update_interactions", 
        json=[
            {
                "user_id": 126706, "book_id": 14433, "progress": 80, "rating": 5, "start_date": "2018-01-01T00:00:00", "used_to_train": True
            }
        ]
    )
    assert response.status_code == 200
    response = client.put(
        "/update_interactions", 
        json=[
            {
                "user_id": "", "book_id": 14433, "progress": 80, "rating": 5, "start_date": "2018-01-01T00:00:00", "used_to_train": True
            }
        ]
    )
    assert response.status_code == 422
