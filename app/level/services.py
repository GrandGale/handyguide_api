from sqlalchemy.orm import Session

from app.level import models, schemas
from app.level.validators import validate_level


def create_level(level: schemas.LevelCreate, db: Session):
    """This function creates a new level in the db

    Args:
        level (schemas.LevelCreate): The LevelCreate schema obj
        db (Session): The DB Session
    """
    validate_level(level=level, db=db)
    obj = models.Level(**level.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
