from sqlalchemy.orm import Session

from app.course import models, schemas
from app.course.validators import validate_course


def create_course(university: str, course: schemas.CourseCreate, db: Session):
    validate_course(university=university, course=course, db=db)
    obj = models.Course(university=university, **course.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
