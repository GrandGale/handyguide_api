from sqlalchemy.orm import Session

from app.department import models


def get_department_list(university: str, faculty_abbrev: str | None, db: Session):
    if faculty_abbrev:
        objs = (
            db.query(models.Department)
            .filter_by(university=university, faculty=faculty_abbrev)
            .all()
        )
    else:
        objs = db.query(models.Department).filter_by(university=university).all()
    return objs


def get_department(university: str, department_abbrev: str, db: Session):
    return (
        db.query(models.Department)
        .filter_by(university=university, abbrev=department_abbrev)
        .first()
    )
