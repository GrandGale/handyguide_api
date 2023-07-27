from sqlalchemy.orm import Session

from app.faculty import models


def get_faculty_list(university: str, db: Session):
    objs = db.query(models.Faculty).filter_by(university=university).all()
    return objs


def get_faculty(university: str, faculty: str, db: Session):
    return (
        db.query(models.Faculty)
        .filter_by(university=university, abbrev=faculty)
        .first()
    )
