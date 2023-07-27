from fastapi import Depends
from sqlalchemy.orm import Session
from app.department import schemas
from app.department.validators import validate_department
from app.dependencies import get_db
from . import models


def create_department(
    university: str,
    department: schemas.DepartmentCreate,
    db: Session = Depends(get_db),
):
    validate_department(university=university, department=department, db=db)
    obj = models.Department(university=university, **department.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
