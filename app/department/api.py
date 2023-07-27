from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config import database
from app.department import selectors, services
from app.dependencies import get_db
from app.faculty.validators import faculty_is_valid
from app.university.validators import university_is_valid
from . import schemas

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
    university_is_valid(university=university, db=db)
    faculty_is_valid(university=university, faculty_abbrev=department.faculty, db=db)
    return services.create_department(
        university=university, department=department, db=db
    )


# Not Needed so far
@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[schemas.Department]
)
def get_faculty_department_list(
    university: str, faculty: str | None = None, db: Session = Depends(get_db)
):
    university_is_valid(university=university, db=db)
    faculty_is_valid(university=university, faculty_abbrev=faculty, db=db)
    return selectors.get_department_list(
        university=university, faculty_abbrev=faculty, db=db
    )
