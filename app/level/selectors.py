from sqlalchemy.orm import Session

from app.level import models


def get_level_list(db: Session):
    """This function returns a list of all the levels in the db

    Args:
        db (Session): The db session

    Returns:
        List[models.Level]: A list of all the levels in the db
    """
    return db.query(models.Level).all()
