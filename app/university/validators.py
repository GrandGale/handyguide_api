from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from . import schemas, models


def university_is_valid(university: str, db: Session = Depends(get_db)):
    if db.query(models.University).get(university):
        return university
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="University Does not exist"
    )