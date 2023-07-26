from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import schemas, models


def create_university(db: Session, university: schemas.UniversityCreate):
    """This function creates a university in the database.

    Args:
        db (Session): The database session.
        university (schemas.UniversityCreate): The university to create.

    Raises:
        HTTPException[409]: If the university already exists.

    Returns:
        models.University: The created university.
    """
    if (
        db.query(models.University)
        .filter_by(name=university.name, abbrev=university.abbrev)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="University Already Exists"
        )
    obj = models.University(**university.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
