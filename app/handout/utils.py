from datetime import datetime
import os
from sqlalchemy.orm import Session
from app.config import settings

from app.course import models as course_models
from app.handout import models


def save_handout(id: int, content: bytes, db: Session) -> bool:
    pass


def local_upload(id: int, content: bytes, db: Session) -> bool:
    directory, filename = gen_path(id=id, db=db)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory + "/" + filename, "wb") as f:
        f.write(content)

    handout = db.query(models.Handout).get(id)
    url = directory.split("media")[1] + "/" + filename
    handout.url = url
    db.add(handout)
    db.commit()
    db.refresh(handout)
    return True


def gen_path(id: int, db: Session) -> str:
    handout = db.query(models.Handout).get(id)
    course = db.query(course_models.Course).filter_by(code=handout.course).first()
    session = settings.SESSION
    university_abbrev = handout.university.upper()
    faculty_abbrev = course.faculty.upper()
    department_abbrev = course.department.upper()
    filename = gen_filename(handout=handout)
    directory = os.path.join(
        settings.MEDIA_DIR,
        "handouts",
        session,
        university_abbrev,
        faculty_abbrev,
        department_abbrev,
        handout.course,
    ).replace("\\", "/")
    return directory, filename


def gen_filename(handout: models.Handout) -> str:
    title = handout.title.replace(" ", "_")
    return f"{handout.id}_{title}.pdf"
