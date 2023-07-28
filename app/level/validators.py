from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.level import schemas, models


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
