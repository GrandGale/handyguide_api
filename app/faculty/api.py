from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.config import database
from app.dependencies import get_db
from app.university.validators import university_is_valid
from . import schemas, services

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Faculty)
def create_faculty(
    faculty: schemas.FacultyCreate,
    university: str,
    db: Session = Depends(get_db),
):
    university_is_valid(db=db, university=university)
    return services.create_faculty(db=db, faculty=faculty, university=university)
