from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.university import models


def university_is_valid(db: Session, university_abbrev: str | None = None):
    """This function checks if the university exists in the db

    Args:
        university_abbrev (str | None): The university abbrev
        db (Session, optional): The DB Session.

    Raises:
        HTTPException[404]: If the university doesnt exist

    Returns:
        bool[True]: If the university exists
    """
    if university_abbrev == None:
        return True
    if db.query(models.University).get(university_abbrev):
        return True
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="University Does not exist"
    )
