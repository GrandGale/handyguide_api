from sqlalchemy.orm import Session

from app.faculty import schemas, models
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
