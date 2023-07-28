from sqlalchemy.orm import Session

from app.course import models


def get_course_list(
    level: str | None,
    university: str | None,
    faculty_abbrev: str | None,
    department_abbrev: str | None,
    db: Session,
):
    """This Function returns a list of courses from a faculty, department or university

    Args:
        level (str | None): The level abbrev
        university (str | None): The university abbrev
        faculty_abbrev (str | None): The faculty abbrev
        department_abbrev (str | None): The department abbrev
        db (Session): The DB Session created

    Returns:
        List[models.Course]: The List of courses that satisfy the criteria specified
    """
    qs = db.query(models.Course)
    if level is not None:
        qs = qs.filter_by(level=level)

    if university is not None:
        qs = qs.filter_by(university=university)

    if faculty_abbrev is not None:
        qs = qs.filter_by(faculty=faculty_abbrev)

    if department_abbrev is not None:
        qs = qs.filter_by(department=department_abbrev)

    return qs.all()


def get_course(university: str, course_code: str, db: Session):
    """This function returns a course

    Args:
        university (str): The university abbrev
        course_code (str): The Course Code
        db (Session): The DB Session created

    Returns:
        models.Course: The Course that fits the above criteria
    """
    return (
        db.query(models.Course)
        .filter_by(university=university, code=course_code)
        .first()
    )
