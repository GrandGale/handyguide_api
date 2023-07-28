from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.faculty import schemas, models


def faculty_is_valid(university: str, faculty_abbrev: str | None, db: Session):
    """This function checks if the faculty exists in the db

    Args:
        university (str): The university abbrev
        faculty_abbrev (str | None): The faculty abbrev
        db (Session): The DB Session

    Raises:
        HTTPException[404]: When the faculty doesnt exist

    Returns:
        bool[True]: If the faculty exists
    """
    if faculty_abbrev == None:
        return None
    elif (
        db.query(models.Faculty)
        .filter_by(abbrev=faculty_abbrev, university=university)
        .first()
    ):
        return True
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Faculty does not exist"
    )


def validate_faculty(
    university: str,
    faculty: schemas.FacultyCreate,
    db: Session,
):
    """This function validates a faculty obj and confirms that it can be saved to the db

    Args:
        university (str): The university abbrev
        faculty (schemas.FacultyCreate): The FacultyCreate schema obj
        db (Session): The DB Session

    Raises:
        HTTPException[409]: When the obj doesnt satisfy the conditions to be saved to the db

    Returns:
        models.Faculty: The created faculty obj
    """
    if (
        db.query(models.Faculty)
        .filter_by(
            name=faculty.name,
            university=university,
        )
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Faculty Already Exists"
        )
    elif (
        db.query(models.Faculty)
        .filter_by(abbrev=faculty.abbrev, university=university)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Faculty with Abbrev already Exists",
        )
    return True
