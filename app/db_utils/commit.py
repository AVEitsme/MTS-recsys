from fastapi.responses import JSONResponse
from app import db
from sqlalchemy.exc import SQLAlchemyError


def commit_transaction() -> JSONResponse:
    """ Try to commit changes in the database;
    Returns:
        Response: Successful operation with code 200 or Internal server error with code 500. 
    """
    try:
        db.commit()
    except SQLAlchemyError as error:
        db.rollback()
        return JSONResponse(content={"message": error._message()}, status_code=500)
    return JSONResponse(content={"message":"Successful operation"}, status_code=200)