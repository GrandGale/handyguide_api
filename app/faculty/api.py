from typing import List
from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import database
from app.dependencies import get_db
from app.faculty import schemas, services, selectors
from app.faculty.validators import faculty_is_valid
from app.university.validators import university_is_valid

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Faculty)
def create_faculty(
    faculty: schemas.FacultyCreate,
    university: str,
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    return services.create_faculty(university=university, faculty=faculty, db=db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Faculty])
def get_faculty_list(university: str, db: Session = Depends(get_db)):
    university_is_valid(university_abbrev=university, db=db)
    return selectors.get_faculty_list(university=university, db=db)


@router.get(
    "/{faculty}", status_code=status.HTTP_200_OK, response_model=schemas.Faculty
)
def get_faculty(university: str, faculty: str, db: Session = Depends(get_db)):
    university_is_valid(university_abbrev=university, db=db)
    faculty_is_valid(university=university, faculty_abbrev=faculty, db=db)
    return selectors.get_faculty(university=university, faculty=faculty, db=db)
