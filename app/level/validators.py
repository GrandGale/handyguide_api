from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.level import schemas, models


def level_is_valid(level_abbrev: str, db: Session):
    """This function checks if the level exists in the db

    Args:
        level_abbrev (str): The level abbrev
        db (Session): The DB Session

    Raises:
        HTTPException[404]: if level doesnt exist in the db

    Returns:
        bool[True]: If level exists in the db
    """
    if level_abbrev == None:
        return True
    if db.query(models.Level).filter_by(abbrev=level_abbrev).first():
        return True
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Level Not Found")


def validate_level(level: schemas.LevelCreate, db: Session):
    """This function validates a level obj and confirms that it can be saved to the db

    Args:
        level (schemas.LevelCreate, optional): The LevelCreate schema obj.
        db (Session): The db session

    Raises:
        HTTPException[409]: When the obj doesnt satisfy the conditions to be saved to the db

    Returns:
        bool[True]: If the LevelCreate obj is valid
    """
    if db.query(models.Level).filter_by(name=level.name).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Level Already Exists"
        )
    elif db.query(models.Level).filter_by(abbrev=level.abbrev).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Level with abbrev Already Exists",
        )
    return True
