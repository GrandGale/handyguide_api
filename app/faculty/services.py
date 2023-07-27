from sqlalchemy.orm import Session

from app.faculty import schemas, models
from app.faculty.validators import validate_faculty


def create_faculty(university: str, faculty: schemas.FacultyCreate, db: Session):
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
    validate_faculty(university=university, faculty=faculty, db=db)
    obj = models.Faculty(**faculty.model_dump(), university=university)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
