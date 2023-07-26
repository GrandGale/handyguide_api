from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import schemas, models


def validate_faculty(db: Session, faculty: schemas.FacultyCreate, university: str):
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
