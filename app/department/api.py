from typing import List
from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import database
from app.department import selectors, services, schemas
from app.dependencies import get_db
from app.department.validators import department_is_valid
from app.faculty.validators import faculty_is_valid
from app.university.validators import university_is_valid

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.Department
)
def create_department(
    university: str,
    department: schemas.DepartmentCreate,
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    faculty_is_valid(university=university, faculty_abbrev=department.faculty, db=db)
    return services.create_department(
        university=university, department=department, db=db
    )


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[schemas.Department]
)
def get_department_list(
    university: str, faculty: str | None = None, db: Session = Depends(get_db)
):
    university_is_valid(university_abbrev=university, db=db)
    faculty_is_valid(university=university, faculty_abbrev=faculty, db=db)
    return selectors.get_department_list(
        university=university, faculty_abbrev=faculty, db=db
    )


@router.get(
    "/{department}", status_code=status.HTTP_200_OK, response_model=schemas.Department
)
def get_department(university: str, department: str, db: Session = Depends(get_db)):
    university_is_valid(university_abbrev=university, db=db)
    department_is_valid(university=university, department_abbrev=department, db=db)
    return selectors.get_department(
        university=university, department_abbrev=department, db=db
    )
