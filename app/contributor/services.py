from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.config.settings import settings
from app.contributor import models, schemas
from app.contributor.security import create_access_token, hash_password, verify_password
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


def login_contributor(contributor: schemas.ContributorLogin, db: Session):
    """This function logs in a contributor

    Args:
        contributor (schemas.ContributorLogin): The contirbutor login schema obj
        db (Session): The DB session

    Returns:
        schemas.Token: The JWT token
    """
    user = authenticate_contributor(
        email=contributor.email, password=contributor.password, db=db
    )
    if user:
        access_token = create_access_token(
            data={
                "sub": user.email,
                "exp": datetime.now()
                + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS),
            }
        )
        return schemas.Token(access_token=access_token, token_type="Bearer")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
    )


def authenticate_contributor(email: str, password: str, db: Session):
    """This function authenticates a contributor

    Args:
        email (str): The contributor's email
        password (str): The contributor's password
        db (Session): The DB session

    Returns:
        bool[False]: If authentication failed
        models.User: The authenticated user obj
    """
    contributor = db.query(models.Contributor).filter_by(email=email).first()
    if contributor and verify_password(raw=password, hashed=contributor.password):
        contributor.last_login = datetime.now()
        db.commit()
        db.refresh(contributor)
        return contributor
    return False
