from app import app, db
from app.database import model
from app.schemas import transaction_responses, db_schema
from app.db_utils import commit_transaction
from typing import List


@app.get("/select_all_interactions", tags=["Interactions"], response_model=List[db_schema.Interaction])
def select_all_interactions(limit: int=None):
    return db.query(model.Interaction).limit(limit).all()

@app.post("/insert_interactions", tags=["Interactions"], responses=transaction_responses)
def insert_interactions(interactions: List[db_schema.Interaction]):
    for interaction in interactions:
        db_interaction = model.Interaction(
            user_id=interaction.user_id,
            book_id=interaction.book_id,
            progress=interaction.progress,
            rating=interaction.rating,
            start_date=interaction.start_date,
            used_to_train=interaction.used_to_train 
        )
        db.add(db_interaction)
    return commit_transaction()

@app.put("/update_ineractions", tags=["Interactions"], responses=transaction_responses)
def update_interactions(interactions: List[db_schema.Interaction]):
    for interaction in interactions:
        db_interaction = db.query(model.Interaction).filter_by(user_id=interaction.user_id, book_id=interaction.book_id).first()
        db_interaction.progress = interaction.progress
        db_interaction.rating = interaction.rating
        db_interaction.start_date = interaction.start_date
        db_interaction.used_to_train = interaction.used_to_train
    return commit_transaction()
