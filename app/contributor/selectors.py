from sqlalchemy.orm import Session

from app.contributor import models


def get_contributor(email: str, db: Session):
    """This function gets a contributor from the database

    Args:
        email (str): The contributor email
        db (Session): The DB session

    Returns:
        models.Contributor: The contributor obj
        None: If the contributor does not exist
    """
    return db.query(models.Contributor).filter_by(email=email).first()
