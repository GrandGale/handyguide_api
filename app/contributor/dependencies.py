from jose import jwt, JWTError
from datetime import datetime
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.contributor import selectors
from app.dependencies import get_db
from app.config.settings import settings
from app.rest_exceptions import InvalidTokenException, ExpiredTokenException


OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="login")


def get_current_contributor(
    token: str = Depends(OAUTH2_SCHEME), db: Session = Depends(get_db)
):
    """This function gets the current contributor"""
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.HASHING_ALGORITHM]
        )
        email: str = payload.get("sub")
        expires: datetime = datetime.fromtimestamp(payload.get("exp"))
        if expires < datetime.now():
            raise ExpiredTokenException
        if email is None:
            raise InvalidTokenException
        contributor = selectors.get_contributor(email=email, db=db)
        return contributor
    except JWTError:
        raise InvalidTokenException
