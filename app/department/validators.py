from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.department import schemas, models


def department_is_valid(university: str, department_abbrev: str | None, db: Session):
    """This function checks if the department exists in the db

    Args:
        university (str): The university abbrev
        department_abbrev (str | None): The department abbrev
        db (Session): The DB Session

    Raises:
        HTTPException[404]: If the department doesnt exist

    Returns:
        bool[True]: If the department exists
    """
    if department_abbrev == None:
        return True

    # Checks if course exists in the DB
    if (
        db.query(models.Department)
        .filter_by(university=university, abbrev=department_abbrev)
        .first()
    ):
        return True

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Department not Found"
    )


def validate_department(
    university: str, department: schemas.DepartmentCreate, db: Session
):
    """This function validates a department obj and confirms that it can be saved to the db

    Args:
        university (str): The university abbrev
        department (schemas.DepartmentCreate): The DepartmentCreate schema obj
        db (Session): The DB Session

    Raises:
        HTTPException[409]: When the obj doesnt satisfy the conditions to be saved to the db

    Returns:
        bool[True]: If the DepartmentCreate obj is valid
    """
    # Checks DB if there is any department with the same name in the university
    if (
        db.query(models.Department)
        .filter_by(name=department.name, university=university)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Department Already Exists"
        )

    # Checks DB if there is any department with the same abbrev in the university
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
