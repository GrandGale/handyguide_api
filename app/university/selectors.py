from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.university import schemas

from . import models


def get_university(db: Session, abbrev: str):
    obj: models.University | None = (
        db.query(models.University).filter(models.University.abbrev == abbrev).first()
    )
    if obj:
        return obj
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="University Not Found"
    )
