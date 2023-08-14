import os
from fastapi import status, HTTPException, Query
from sqlalchemy.orm import Session
from app.config.settings import settings

from app.handout import models


def get_handout_list(
    university: str | None,
    faculty: str | None,
    department: str | None,
    course: str | None,
    search: str | None,
    level: str | None,
    db: Session,
):
    if search:
        search = search.lower()
        qs = db.query(models.Handout).filter(
            models.Handout.title.contains(search)
        ) or db.query(models.Handout).filter(models.Handout.course.contains(search))
        return qs.all()
    qs = db.query(models.Handout)
    if university:
        qs = qs.filter_by(university=university)

    if faculty and university:
        qs = qs.filter_by(university=university, faculty=faculty)

    elif department and university:
        qs = qs.filter_by(university=university, department=department)

    elif course and university:
        qs = qs.filter_by(university=university, course=course)

    elif not university:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You must provide a university",
        )
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
