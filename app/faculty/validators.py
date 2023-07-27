from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.faculty import schemas, models


def faculty_is_valid(university: str, faculty_abbrev: str | None, db: Session):
    if faculty_abbrev == None:
        return None
    elif (
        db.query(models.Faculty)
        .filter_by(abbrev=faculty_abbrev, university=university)
        .first()
    ):
        return faculty_abbrev
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
