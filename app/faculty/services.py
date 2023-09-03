from fastapi import status, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.faculty import schemas, selectors, models
from app.faculty.validators import validate_faculty


def create_faculty(university: str, faculty: schemas.FacultyCreate, db: Session):
    """This function creates a faculty in the db

    Args:
        university (str): The university to create the faculty in
        faculty (schemas.FacultyCreate): The faculty obj to create
        db (Session): The DB Session

    Returns:
        models.Faculty: The created faculty obj
    """
    validate_faculty(university=university, faculty=faculty, db=db)
    obj = models.Faculty(**faculty.model_dump(), university=university)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def edit_faculty(
    university: str, faculty_abbrev: str, update: schemas.FacultyUpdate, db: Session
):
    faculty = selectors.get_faculty(
        university=university, faculty=faculty_abbrev, db=db
    )
    if faculty:
        for field, value in update.model_dump().items():
            if value is not None:
                setattr(faculty, field, value)
        db.add(faculty)
        db.commit()
        db.refresh(faculty)
        return faculty
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Faculty not found"
    )
