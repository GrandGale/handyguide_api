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


def handout_id_is_valid(id: int, db: Session):
    """This function validates a handout id and confirms that it exists in the db

    Args:
        id (int): The handout id
        db (Session): The DB session

    Raises:
        HTTPException[404]: When the id doesnt exist in the db

    Returns:
        bool[True]: If the id is valid
    """
    if db.query(models.Handout).get(id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Handout Not Found"
        )
    return True
