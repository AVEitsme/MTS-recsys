from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_age = Column(String, nullable=True)
    user_sex = Column(Boolean, nullable=True)


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    book_title = Column(String, nullable=False)
    book_year = Column(String, nullable=True)
    

class Interaction(Base):
    __tablename__ = "interactions"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.book_id"), primary_key=True, index=True)
    progress = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=True)
    start_date = Column(DateTime, nullable=False)
    used_to_train = Column(Boolean, nullable=False)
