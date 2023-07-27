from typing import List
from sqlalchemy.orm import Session

from app.course import models


def get_course_list(
    university: str,
    faculty_abbrev: str | None,
    department_abbrev: str | None,
    db: Session,
):
    qs = db.query(models.Course).filter_by(university=university)

    if faculty_abbrev is not None:
        qs = qs.filter_by(faculty=faculty_abbrev)

    if department_abbrev is not None:
        qs = qs.filter_by(department=department_abbrev)

    return qs.all()


def get_course(university: str, course_code: str, db: Session):
    return (
        db.query(models.Course)
        .filter_by(university=university, code=course_code)
        .first()
    )
