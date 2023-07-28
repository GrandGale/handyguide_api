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
    """This function creates a new department entry in the db

    Args:
        university (str): The unievrsity abbrev
        department (schemas.DepartmentCreate): The department obj
        db (Session): The DB Session

    Returns:
        models.Department: The created Department obj
    """
    validate_department(university=university, department=department, db=db)
    obj = models.Department(university=university, **department.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
