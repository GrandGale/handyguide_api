from sqlalchemy.orm import Session

from app.handout import schemas, models
from app.handout.validators import validate_handout


def create_handout(university: str, handout: schemas.HandoutCreate, db: Session):
    """This function creates a handout and saves it to the db

    Args:
        handout (schemas.HandoutCreate): The HandoutCreate schema obj
        university (str): The university abbrev
        db (Session, optional): The DB Session

    Returns:
        schemas.Handout: The Handout schema obj
    """
    validate_handout(university=university, handout=handout, db=db)
    obj = models.Handout(university=university, **handout.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
