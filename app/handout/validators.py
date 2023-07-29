from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.handout import models, schemas


def validate_handout(university: str, handout: schemas.HandoutCreate, db: Session):
    """This function validates a handout obj and confirms that it can be saved to the db

    Args:
        handout (schemas.HandoutCreate, optional): The HandoutCreate schema obj.
        db (Session): The db session

    Raises:
        HTTPException[409]: When the obj doesnt satisfy the conditions to be saved to the db

    Returns:
        bool[True]: If the HandoutCreate obj is valid
    """
    if db.query(models.Handout).filter_by(title=handout.title).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Handout With Title Already Exists",
        )
    return True
