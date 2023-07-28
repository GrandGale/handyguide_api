from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.university import models


def get_university_list(db: Session):
    """This function returns a list of all universities in the database.

    Args:
        db (Session): The database session.

    Returns:
        List[models.University]: A list of all universities in the database.
    """
    objs: List[models.University] = db.query(models.University).all()
    return objs


def get_university(university_abbrev: str, db: Session):
    """This function returns a university from the database.

    Args:
        universirty_abbrev (str): The abbreviation of the university to return.
        db (Session): The database session.

    Raises:
        HTTPException[404]: If the university is not found.

    Returns:
        models.University: The university obj from the database.
    """
    obj: models.University | None = (
        db.query(models.University).filter_by(abbrev=university_abbrev).first()
    )
    if obj:
        return obj
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="University Not Found"
    )
