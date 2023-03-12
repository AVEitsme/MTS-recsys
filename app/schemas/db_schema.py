from pydantic import BaseModel
from typing import Union, Literal
from datetime import datetime


class User(BaseModel):

    user_id: int
    user_age: Union[Literal["18_24", "25_34", "35_44", "45_54", "55_64", "65_inf"], None] # <-- weak
    user_sex: Union[bool, None]
    
    class Config:
        orm_mode = True


class Book(BaseModel):
        
    book_id: int
    book_title: str
    book_year: Union[str, None]

    class Config:
        orm_mode = True


class Interaction(BaseModel):
    user_id: int
    book_id: int
    progress: int
    rating: Union[Literal[1, 2, 3, 4, 5], None]
    start_date: datetime
    used_to_train: bool

    class Config:
        orm_mode = True
