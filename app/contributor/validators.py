from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.contributor import models, schemas


def validate_contributor(contributor: schemas.ContributorCreate, db: Session):
    """This function validates the contributor data and confirms that it can be saved to db

    Args:
        contributor (schemas.ContributorCreate): The contributor schema obj
        db (Session): The DB Session

    Raises:
        HTTPException[409]: When the obj doesnt satisfy the conditions to be saved to db

    Returns:
       bool[True]: If the ContributorCreate obj is valid
    """
    # Check if username is taken
    if db.query(models.Contributor).filter_by(username=contributor.username).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username taken"
        )

    # Check if email is taken
    elif db.query(models.Contributor).filter_by(email=contributor.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email taken")

    # Check if university_id is being used in the same university
    elif (
        db.query(models.Contributor)
        .filter_by(
            university=contributor.university, university_id=contributor.university_id
        )
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="University ID is being used by another contributor in the university",
        )

    return True
