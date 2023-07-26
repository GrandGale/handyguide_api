from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db

from . import schemas, models


def faculty_is_valid(university: str, faculty: str, db: Session):
    if (
        db.query(models.Faculty)
        .filter_by(university=university, abbrev=faculty)
        .first()
    ):
        return faculty
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Faculty does not exist"
    )


def validate_faculty(
    university: str,
    faculty: schemas.FacultyCreate,
    db: Session,
):
    if (
        db.query(models.Faculty)
        .filter_by(
            name=faculty.name,
            abbrev=faculty.abbrev,
            university=university,
        )
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Faculty Already Exists"
        )
    return True
