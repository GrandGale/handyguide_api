from typing import List
from fastapi import status, HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from app.contributor.dependencies import get_current_contributor

from app.dependencies import get_db
from app.contributor import models as contributor_models
from app.faculty import schemas, services, selectors
from app.faculty.validators import faculty_is_valid
from app.university.validators import university_is_valid

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
def get_faculty(university: str, faculty: int, db: Session = Depends(get_db)):
    university_is_valid(university_abbrev=university, db=db)
    faculty_is_valid(university=university, faculty_id=faculty, db=db)
    return selectors.get_faculty(university=university, faculty=faculty, db=db)


@router.put(
    "/{faculty}/edit",
    status_code=status.HTTP_200_OK,
    response_model=schemas.Faculty,
)
def edit_faculty(
    faculty: str,
    university: str,
    update: schemas.FacultyUpdate,
    contributor: contributor_models.Contributor = Depends(get_current_contributor),
    db: Session = Depends(get_db),
):
    if contributor.is_supervisor or contributor.is_admin:
        university_is_valid(university_abbrev=university, db=db)
        return services.edit_faculty(
            university=university, faculty_abbrev=faculty, update=update, db=db
        )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You do not have permission to edit this faculty",
    )
