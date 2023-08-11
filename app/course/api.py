from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.course import schemas, services, selectors
from app.course.validators import course_is_valid
from app.department.validators import department_is_valid
from app.faculty.validators import faculty_is_valid
from app.university.validators import university_is_valid

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


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Course])
def get_course_list(
    level: str | None = None,
    university: str | None = None,
    faculty: str | None = None,
    department: str | None = None,
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    faculty_is_valid(university=university, faculty_abbrev=faculty, db=db)
    department_is_valid(university=university, department_abbrev=department, db=db)
    return selectors.get_course_list(
        level=level,
        university=university,
        faculty_abbrev=faculty,
        department_abbrev=department,
        db=db,
    )


@router.get(
    "/{course}", status_code=status.HTTP_200_OK, response_model=schemas.CourseDetail
)
def get_course(university: str, course: str, db: Session = Depends(get_db)):
    university_is_valid(university_abbrev=university, db=db)
    course_is_valid(university=university, course_code=course, db=db)
    return selectors.get_course(university=university, course_code=course, db=db)
