from sqlalchemy.orm import Session

from app.contributor import models, schemas
from app.contributor.security import hash_password
from app.contributor.validators import validate_contributor


def create_contributor(contributor: schemas.ContributorCreate, db: Session):
    """This function creates a new contributor entry in the database

    Args:
        contributor (schemas.ContributorCreate): The contributor obj
        db (Session): The DB session

    Returns:
        models.Contributor: The created contributor obj
    """
    validate_contributor(contributor=contributor, db=db)
    obj = models.Contributor(**contributor.model_dump())
    obj.password = hash_password(raw=contributor.password)
    obj.is_contributor = True
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
