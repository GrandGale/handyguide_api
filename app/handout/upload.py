import os
import logging
from fastapi import status, UploadFile, HTTPException
from sqlalchemy.orm import Session

from azure.storage.blob import BlobClient

from app.config.settings import settings, MEDIA_DIR
from app.handout import models
from app.course import models as course_models
from app.department import models as department_models
from app.faculty import models as faculty_models


# logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


async def upload_handout(id: int, file: UploadFile, dir: str, db: Session) -> str:
    handout = db.query(models.Handout).get(id)
    if settings.DEBUG:
        url = local_upload(id=id, file=file, dir=dir, db=db)
        return url
    else:
        try:
            blob = BlobClient.from_connection_string(
                conn_str=settings.AZURE_CONNECTION_STRING,
                container_name=settings.AZURE_CONTAINER_NAME,
                blob_name=f"{dir}/{gen_filename(handout_id=id, db=db)}.pdf",
            )
            blob.upload_blob(file.file, overwrite=True)
            url = blob.url
            handout.url = url.split("handouts")[1]
            print(handout.url)
            db.add(handout)
            db.commit()
            db.refresh(handout)

        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal Server Error: Error while uploading file",
            )

        return blob.url


def local_upload(id: int, file: UploadFile, dir: str, db: Session) -> str:
    handout = db.query(models.Handout).get(id)
    filename = gen_filename(handout_id=id, db=db)
    dir = os.path.join(MEDIA_DIR, dir)
    if not os.path.exists(dir):
        os.makedirs(dir)

    with open(f"{dir}/{filename}.pdf", "wb") as f:
        contents = file.file.read()
        f.write(contents)

    url = dir.split("media")[1] + "/" + filename
    handout.url = url
    db.add(handout)
    db.commit()
    db.refresh(handout)
    return dir + "/" + filename


def gen_path(id: int, db: Session) -> str:
    handout = db.query(models.Handout).get(id)
    session = settings.SESSION
    university_abbrev = handout.university.upper()
    faculty_abbrev = (
        db.query(faculty_models.Faculty).get(handout.faculty).abbrev.upper()
    )
    department_abbrev = (
        db.query(department_models.Department).get(handout.department).abbrev.upper()
    )
    course_code = db.query(course_models.Course).get(handout.course).code
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
