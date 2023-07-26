from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config import database
from app.department import services
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
    faculty: str,
    department: schemas.DepartmentCreate,
    db: Session = Depends(get_db),
):
    university_is_valid(university=university, db=db)
    faculty_is_valid(university=university, faculty=faculty, db=db)
    return services.create_department(
        university=university, faculty=faculty, department=department, db=db
    )
