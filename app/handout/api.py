from typing import List
from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import database
from app.course.validators import course_is_valid
from app.handout import selectors, services, schemas
from app.dependencies import get_db
from app.university.validators import university_is_valid

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Handout)
async def create_handout(
    university: str,
    handout: schemas.HandoutCreate,
    db: Session = Depends(get_db),
):
    """This function creates a handout and saves it to the db

    Args:
        handout (schemas.HandoutCreate): The HandoutCreate schema obj
        university (str): The university abbrev
        db (Session, optional): The DB Session

    Returns:
        schemas.Handout: The Handout schema obj
    """
    university_is_valid(university_abbrev=university, db=db)
    course_is_valid(university=university, course_code=handout.course, db=db)
    return services.create_handout(university=university, handout=handout, db=db)
