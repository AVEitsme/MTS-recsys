from app import app, db
from app.database import model
from app.schemas import transaction_responses, db_schema
from app.db_utils import commit_transaction
from typing import List


@app.get("/select_all_users", tags=["Users"], response_model=List[db_schema.User])
def select_all_users(limit: int=None):
    return db.query(model.User).limit(limit).all()

@app.post("/insert_users", tags=["Users"], responses=transaction_responses)
def insert_users(users: List[db_schema.User]):
    for user in users:
        db_user = model.User(user_id=user.user_id, user_age=user.user_age, user_sex=user.user_sex)
        db.add(db_user)
    return commit_transaction()

@app.put("/update_users", tags=["Users"], responses=transaction_responses)
def update_users(users: List[db_schema.User]):
    for user in users:
        db_user = db.query(model.User).filter_by(user_id=user.user_id).first()
        db_user.user_age = user.user_age
        db_user.user_sex = user.user_sex
    return commit_transaction()