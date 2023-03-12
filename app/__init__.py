from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.database import SessionLocal


app = FastAPI()
db = SessionLocal()

from app.routes import *


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")
