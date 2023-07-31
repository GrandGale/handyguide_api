import os
from fastapi import status, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.handout import schemas, models, utils
from app.handout.validators import validate_handout


def create_handout(university: str, handout: schemas.HandoutCreate, db: Session):
    """This function creates a handout and saves it to the db

    Args:
        handout (schemas.HandoutCreate): The HandoutCreate schema obj
        university (str): The university abbrev
        db (Session, optional): The DB Session

    Returns:
        schemas.Handout: The Handout schema obj
    """
    validate_handout(university=university, handout=handout, db=db)
    obj = models.Handout(university=university, **handout.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def upload_handout(id: int, file: UploadFile, db: Session):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_DIR = os.path.join(BASE_DIR, f"media\\handouts\\")
    """This function uploads a handout to the server

    Args:
        id (int): The id of the handout
        file (UploadFile): The file to be uploaded

    Returns:
        schemas.Handout: The Handout schema obj
    """
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="File must be a pdf",
        )

    content = file.file.read()
    utils.save_handout(id=id, content=content, db=db)

    return True
