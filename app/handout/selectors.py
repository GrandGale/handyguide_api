import os
from sqlalchemy.orm import Session

from app.config.settings import settings
from app.handout import models
from app.course import models as course_models
from app.utils.paginators import paginate


def get_handout_list(
    university: str | None,
    faculty: int | None,
    department: int | None,
    course: int | None,
    level: str | None,
    page: int,
    size: int,
    db: Session,
):
    qs = db.query(models.Handout)
    if university:
        qs = qs.filter_by(university=university)
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

    return paginate(qs=qs, page=page, size=size)


def handout_search(q: str, university: str | None, page: int, size: int, db: Session):
    handouts = []
    courses_qs = db.query(course_models.Course).filter(
        (course_models.Course.name.ilike(f"%{q}%"))
        | (course_models.Course.code.ilike(f"%{q}%"))
    )
    if courses_qs:
        for course in courses_qs.all():
            handouts.extend(db.query(models.Handout).filter_by(course=course.id).all())

    handouts = db.query(models.Handout).filter(models.Handout.title.ilike(f"%{q}%"))
    if university:
        handouts = handouts.filter_by(university=university)

    return paginate(qs=handouts, page=page, size=size)
