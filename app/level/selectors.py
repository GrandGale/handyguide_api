from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.level import models


def get_level_list(db: Session):
    """This function returns a list of all the levels in the db

    Args:
        db (Session): The db session

    Returns:
        List[models.Level]: A list of all the levels in the db
    """
    return db.query(models.Level).all()


def get_level(level_abbrev: str, db: Session):
    """This function returns a level obj from the db

    Args:
        level_abbrev (str): The level abbrev
        db (Session): The db session

    Raises:
        HTTPException[404]: If the level doesnt exist

    Returns:
        models.Level: The level obj
    """
    level = db.query(models.Level).filter_by(abbrev=level_abbrev).first()
    if not level:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Level Not Found"
        )
    return level
