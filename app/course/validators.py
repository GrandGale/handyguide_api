# NOTE: THOROUGHLY TEST BEFORE MAKING ANY CHANGES TO A VALIDATOR

from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.course import models, schemas


def course_is_valid(university: str, course_code: str | None, db: Session):
    """This function checks if the course is a valid course in the DB

    Args:
        university (str): The university the course belongs to
        course_code (str | None): The course code
        db (Session): The DB Session created

    Raises:
        HTTPException[404]: When the course doesnt exist

    Returns:
        bool[True]: if the course is valid
    """
    if course_code == None:
        return True

    # Checks if course exists in db
    if db.query(models.Course).filter_by(university=university, code=course_code):
        return True
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Course not Found"
    )


def validate_course(university: str, course: schemas.CourseCreate, db: Session):
    """This function validates a course obj and confirms that it can be saved to the db

    Args:
        university (str): The university abbrev
        course (schemas.CourseCreate): The CourseCreate schema obj
        db (Session): The DB Session

    Raises:
        HTTPException: When the obj doesnt satisfy the conditions to be saved to the db

    Returns:
        bool[True]: If the CourseCreate obj is valid
    """
    # Checks DB if there is any course with the same name in the university
    if (
        db.query(models.Course)
        .filter_by(name=course.name, university=university)
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course with Name Already Exists",
        )

    # Checks DB if there is any course with the same code in the university
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
