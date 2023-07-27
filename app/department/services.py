from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.department import schemas, models
from app.department.validators import validate_department


def create_department(
    university: str,
    department: schemas.DepartmentCreate,
    db: Session,
):
    validate_department(university=university, department=department, db=db)
    obj = models.Department(university=university, **department.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
