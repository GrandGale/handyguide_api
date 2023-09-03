from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.department import schemas, selectors, models
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


def edit_department(
    university: str,
    department_abbrev: str,
    update: schemas.DepartmentUpdate,
    db: Session,
):
    """This function edits a department entry in the db

    Args:
        university (str): The university abbrev
        department_abbrev (str): The department abbrev
        update (schemas.DepartmentUpdate): The update obj
        db (Session): The DB Session

    Returns:
        models.Department: The updated Department obj
    """
    department = selectors.get_department(
        university=university, department_abbrev=department_abbrev, db=db
    )
    if department:
        try:
            validate_department(university=university, department=update, db=db)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Department with details already exists",
            )
        for field, value in update.model_dump().items():
            if value is not None:
                setattr(department, field, value)
        db.add(department)
        db.commit()
        db.refresh(department)
        return department
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Department not found"
    )
