from sqlalchemy.orm import Session

from app.faculty.validators import validate_faculty

from . import schemas, models


def create_faculty(db: Session, university: str, faculty: schemas.FacultyCreate):
    """This function creates a faculty in the database.

    Args:
        db (Session): The database session.
        faculty (schemas.FacultyCreate): The faculty to create.
        university: the abbreviation of the university that the faculty belongs to

    Raises:
        HTTPException[409]: If the faculty already exists.

    Returns:
        models.Faculty: The created faculty.
    """
    validate_faculty(db=db, faculty=faculty, university=university)
    obj = models.Faculty(**faculty.model_dump(), university=university)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
