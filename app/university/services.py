from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import schemas, models


def create_university(db: Session, university: schemas.UniversityCreate):
    if (
        db.query(models.University)
        .filter_by(name=university.name, abbrev=university.abbrev)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="University Already Exists"
        )
    obj = models.University(**university.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
