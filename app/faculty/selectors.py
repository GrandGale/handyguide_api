from sqlalchemy.orm import Session

from app.faculty import models


def get_faculty_list(university: str, db: Session):
    """This function returns a list of all faculties in a university.

    Args:
        university (str): The university to get the faculties from.
        db (Session): The DB session.

    Returns:
        List[models.Faculty]: The list of faculties.
    """
    objs = db.query(models.Faculty).filter_by(university=university).all()
    return objs


def get_faculty(university: str, faculty: str, db: Session):
    """This function returns a faculty from the database.

    Args:
        university (str): The university to get the faculty from.
        faculty (str): The faculty abbrev
        db (Session): The DB session.

    Returns:
        models.Faculty: The faculty.
    """
    return (
        db.query(models.Faculty)
        .filter_by(university=university, abbrev=faculty)
        .first()
    )
