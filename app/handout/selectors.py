import os
from fastapi import status, HTTPException, Query
from sqlalchemy.orm import Session

from app.config.settings import settings
from app.handout import models
from app.course import models as course_models


def get_handout_list(
    university: str,
    faculty: int | None,
    department: int | None,
    course: int | None,
    level: str | None,
    db: Session,
):
    qs = db.query(models.Handout).filter_by(university=university)
    if faculty:
        qs = qs.filter_by(faculty=faculty)
    if department:
        qs = qs.filter_by(department=department)
    if course:
        qs = qs.filter_by(course=course)
    if level:
        qs = qs.filter_by(level=level)

    if settings.DEBUG:
        base = os.getcwd().replace("\\", "/")
        for obj in qs.all():
            obj.url = f"{base}/app/media/{obj.url}.pdf"
    else:
        for obj in qs.all():
            obj.url = f"{settings.AZURE_BLOB_URL}{obj.url}"

    return qs.all()
