from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import database
from app.dependencies import get_db
from app.university import schemas, services, selectors

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.University
)
def create_university(
    university: schemas.UniversityCreate,
    db: Session = Depends(get_db),
):
    return services.create_university(university=university, db=db)


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=list[schemas.University]
)
def get_university_list(db: Session = Depends(get_db)):
    return selectors.get_university_list(db=db)


@router.get(
    "/{university}", status_code=status.HTTP_200_OK, response_model=schemas.University
)
def get_university(university: str, db: Session = Depends(get_db)):
    return selectors.get_university(university_abbrev=university, db=db)
