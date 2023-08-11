import os
import logging
from fastapi import status, UploadFile, HTTPException
from sqlalchemy.orm import Session

from azure.storage.blob import BlobClient

from app.config.settings import settings, MEDIA_DIR
from app.course import models as course_models
from app.handout import models


# logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


async def upload_handout(id: int, file: UploadFile, dir: str, db: Session) -> str:
    if settings.DEBUG:
        local_upload(id=id, file=file, dir=dir, db=db)
    else:
        try:
            blob = BlobClient.from_connection_string(
                conn_str=settings.AZURE_CONNECTION_STRING,
                container_name=settings.AZURE_CONTAINER_NAME,
                blob_name=f"{dir}/{gen_filename(handout_id=id, db=db)}.pdf",
            )
            blob.upload_blob(file.file, overwrite=True)

        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal Server Error: Error while uploading file",
            )
    
    return blob.url


def local_upload(id: int, file: UploadFile, dir: str, db: Session) -> bool:
    handout = db.query(models.Handout).get(id)
    filename = gen_filename(handout_id=id, db=db)
    dir = os.path.join(MEDIA_DIR, dir)
    if not os.path.exists(dir):
        os.makedirs(dir)

    with open(dir + "/" + filename, "wb") as f:
        contents = file.file.read()
        f.write(contents)

    url = dir.split("media")[1] + "/" + filename
    handout.url = url
    db.add(handout)
    db.commit()
    db.refresh(handout)
    return True


def gen_path(id: int, db: Session) -> str:
    handout = db.query(models.Handout).get(id)
    session = settings.SESSION
    university_abbrev = handout.university.upper()
    faculty_abbrev = handout.faculty.upper()
    department_abbrev = handout.department.upper()
    course_code = handout.course
    directory = os.path.join(
        session,
        university_abbrev,
        faculty_abbrev,
        department_abbrev,
        course_code,
    ).replace("\\", "/")
    return directory


def gen_filename(handout_id: int, db: Session) -> str:
    handout = db.query(models.Handout).get(handout_id)
    title = handout.title.replace(" ", "_")
    return f"{handout.id}_{title}"
