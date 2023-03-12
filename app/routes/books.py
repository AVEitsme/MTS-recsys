from app import app, db
from app.database import model
from app.schemas import transaction_responses, db_schema
from app.db_utils import commit_transaction
from typing import List

tags = ["Books"]

@app.get("/select_all_books", tags=tags, response_model=List[db_schema.Book])
def select_all_books(limit: int=None):
    return db.query(model.Book).limit(limit).all()

@app.post("/select_books_by_ids", tags=tags, response_model=List[db_schema.Book])
def select_books_by_ids(ids: List[int]):
    return db.query(model.Book).filter(model.Book.book_id.in_(ids)).all()

@app.post("/insert_books", tags=tags, responses=transaction_responses)
def insert_books(books: List[db_schema.Book]):
    for book in books:
        db_book = model.Book(book_id=book.book_id, book_title=book.book_title, book_year=book.book_year)
        db.add(db_book)
    return commit_transaction()

@app.put("/update_books", tags=tags, responses=transaction_responses)
def update_books(books: List[db_schema.Book]):
    for book in books:
        db_book = db.query(model.Book).filter_by(book_id=book.book_id).first()
        db_book.book_title = book.book_title
        db_book.book_year = book.book_year
    return commit_transaction()