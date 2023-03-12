from app import app, db
from app.database import model
from app.schemas import transaction_responses, db_schema
from app.db_utils import commit_transaction
from typing import List

tags = ["Users"]

@app.get("/select_all_users", tags=tags, response_model=List[db_schema.User])
def select_all_users(limit: int=None):
    return db.query(model.User).limit(limit).all()

@app.post("/select_users_by_ids", tags=tags, response_model=List[db_schema.User])
def select_users_by_ids(ids: List[int]):
    return db.query(model.User).filter(model.User.user_id.in_(ids)).all()

@app.post("/insert_users", tags=tags, responses=transaction_responses)
def insert_users(users: List[db_schema.User]):
    for user in users:
        db_user = model.User(user_id=user.user_id, user_age=user.user_age, user_sex=user.user_sex)
        db.add(db_user)
    return commit_transaction()

@app.put("/update_users", tags=tags, responses=transaction_responses)
def update_users(users: List[db_schema.User]):
    for user in users:
        db_user = db.query(model.User).filter_by(user_id=user.user_id).first()
        db_user.user_age = user.user_age
        db_user.user_sex = user.user_sex
    return commit_transaction()