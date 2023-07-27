from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.course import models, schemas


def course_is_valid(university: str, course_code: str | None, db: Session):
    if course_code == None:
        return True
    if db.query(models.Course).filter_by(university=university, code=course_code):
        return course_code
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Course not Found"
    )


def validate_course(university: str, course: schemas.CourseCreate, db: Session):
    if (
        db.query(models.Course)
        .filter_by(name=course.name, university=university)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course with Name Already Exists",
        )
    elif (
        db.query(models.Course)
        .filter_by(code=course.code, university=university)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course with Code Already Exists",
        )
    return True
