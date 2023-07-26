from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session
from app import dependencies as global_dependencies
from app.university import selectors

from . import schemas, services
from app.config import database

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.University
)
def create_university(
    university: schemas.UniversityCreate,
    db: Session = Depends(global_dependencies.get_db),
):
    return services.create_university(db=db, university=university)


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=list[schemas.University]
)
def get_university_list(db: Session = Depends(global_dependencies.get_db)):
    return selectors.get_university_list(db=db)


@router.get(
    "/{abbrev}", status_code=status.HTTP_200_OK, response_model=schemas.University
)
def get_university(abbrev: str, db: Session = Depends(global_dependencies.get_db)):
    return selectors.get_university(db=db, abbrev=abbrev)
