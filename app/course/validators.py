from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.course import models, schemas


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
