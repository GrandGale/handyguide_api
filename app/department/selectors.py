from sqlalchemy.orm import Session

from app.department import models


def get_department_list(university: str, faculty_abbrev: str | None, db: Session):
    """This function returns a list of Departments belonging to a university, faculty or department

    Args:
        university (str): The university abbrev
        faculty_abbrev (str | None): The faculty abbrev
        db (Session): The DB Session

    Returns:
        List[models.Department]: A list of departments that satisfy the criteria specified
    """
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
    """This functions returns a department obj

    Args:
        university (str): The university the department belongs to
        department_abbrev (str): The department abbrev
        db (Session): The DB Session

    Returns:
        models.Deparment: The Department obj
    """
    return (
        db.query(models.Department)
        .filter_by(university=university, abbrev=department_abbrev)
        .first()
    )
