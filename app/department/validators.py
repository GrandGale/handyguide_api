from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.department import schemas
from . import models, schemas


def department_is_valid(university: str, department: str, db: Session):
    if (
        db.query(models.Department)
        .filter_by(university=university, abbrev=department)
        .first()
    ):
        return department
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Department not Found"
    )


def validate_department(
    university: str, department: schemas.DepartmentCreate, db: Session
):
    if (
        db.query(models.Department)
        .filter_by(university=university, **department.model_dump())
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Department Already Exists"
        )
    return True
