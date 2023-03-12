from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_select_all_books():
    response = client.get("/select_all_books", params={"limit": 10})
    assert response.status_code == 200

def test_select_books_by_ids():
    response = client.post("/select_books_by_ids", json=[1, 2, 3])
    assert response.status_code == 200
    response = client.post("/select_books_by_ids", json=[1, 2, "a"])
    assert response.status_code == 422

def test_insert_books():
    response = client.post("/insert_books", json=[{"book_id": 1, "book_title": "Bible", "book_year": ""}])
    assert response.status_code == 500
    response = client.post("/insert_books", json=[{"book_id": "a", "book_title": "Bible", "book_year": ""}])
    assert response.status_code == 422

def test_update_books():
    response = client.put("/update_books", json=[{"book_id": 1, "book_title": "Множественные источники дохода", "book_year": "2011"}])
    assert response.status_code == 200
    response = client.put("/update_books", json=[{"book_id": "a", "book_title": "Множественные источники дохода", "book_year": "2011"}])
    assert response.status_code == 422