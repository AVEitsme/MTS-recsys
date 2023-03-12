from pydantic import BaseModel


class Message(BaseModel):
    message: str


transaction_responses = {
    200: {"model": Message},
    500: {"model": Message}
}