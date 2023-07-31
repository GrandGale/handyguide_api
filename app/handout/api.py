from typing import List
from fastapi import UploadFile, status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import database
from app.course.validators import course_is_valid
from app.handout import selectors, services, schemas
from app.dependencies import get_db
from app.handout.validators import handout_id_is_valid
from app.university.validators import university_is_valid

database.DBBase.metadata.create_all(bind=database.engine)
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
