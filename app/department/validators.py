from fastapi import HTTPException, status
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session

from app.department import schemas
from . import models, schemas


def department_is_valid(university: str, department_abbrev: str | None, db: Session):
    if department_abbrev == None:
        return True
    if (
        db.query(models.Department)
        .filter_by(university=university, abbrev=department_abbrev)
        .first()
    ):
        return department_abbrev

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Department not Found"
    )


def validate_department(
    university: str, department: schemas.DepartmentCreate, db: Session
):
    if (
        db.query(models.Department)
        .filter_by(name=department.name, university=university)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Department Already Exists"
        )
    elif (
        db.query(models.Department)
        .filter_by(abbrev=department.abbrev, university=university)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Department with Abbreviation already Exists",
        )
    return True
