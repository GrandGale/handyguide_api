from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.course import schemas, services
from app.department.validators import department_is_valid
from app.dependencies import get_db
from app.faculty.validators import faculty_is_valid
from app.university.validators import university_is_valid

from ..config import database

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Course)
def create_course(
    university: str,
    course: schemas.CourseCreate,
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    faculty_is_valid(university=university, faculty_abbrev=course.faculty, db=db)
    department_is_valid(
        university=university, department_abbrev=course.department, db=db
    )
    return services.create_course(university=university, course=course, db=db)
