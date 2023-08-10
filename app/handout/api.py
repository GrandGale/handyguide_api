from typing import List
from fastapi import UploadFile, status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.course.validators import course_is_valid
from app.department.validators import department_is_valid
from app.faculty.validators import faculty_is_valid
from app.handout import selectors, services, schemas
from app.dependencies import get_db
from app.handout.validators import handout_id_is_valid
from app.level.validators import level_is_valid
from app.university.validators import university_is_valid

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Handout)
def create_handout(
    university: str,
    handout: schemas.HandoutCreate,
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    course_is_valid(university=university, course_code=handout.course, db=db)
    return services.create_handout(university=university, handout=handout, db=db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def upload_handout(id: int, file: UploadFile, db: Session = Depends(get_db)):
    handout_id_is_valid(id=id, db=db)
    obj = services.upload_handout(id=id, file=file, db=db)
    return obj


@router.get("/", response_model=List[schemas.Handout])
def get_handout_list(
    university: str | None = None,
    faculty: str | None = None,
    department: str | None = None,
    course: str | None = None,
    search: str | None = None,
    level: str | None = None,
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    faculty_is_valid(university=university, faculty_abbrev=faculty, db=db)
    department_is_valid(university=university, department_abbrev=department, db=db)
    course_is_valid(university=university, course_code=course, db=db)
    level_is_valid(level_abbrev=level, db=db)
    return selectors.get_handout_list(
        university=university,
        faculty=faculty,
        department=department,
        course=course,
        search=search,
        level=level,
        db=db,
    )
