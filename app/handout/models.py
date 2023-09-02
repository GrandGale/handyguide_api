from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, UniqueConstraint

from app.config.database import DBBase
from app.config.settings import settings
from app.contributor.models import Contributor
from app.course.models import Course
from app.department.models import Department
from app.faculty.models import Faculty
from app.university.models import University


class Handout(DBBase):
    __tablename__ = "handouts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), index=True, nullable=False)
    url = Column(String, default="/", nullable=False)
    upload_date = Column(DateTime, index=True, default=datetime.now(), nullable=False)
    university = Column(String(10), ForeignKey(University.abbrev), nullable=False)
    faculty = Column(String(10), ForeignKey(Faculty.abbrev), nullable=False)
    department = Column(String(10), ForeignKey(Department.abbrev), nullable=False)
    course = Column(String(10), ForeignKey(Course.code), nullable=False)
    session = Column(String, default=settings.SESSION, nullable=False)
    level = Column(Integer, nullable=False)
    contributor = Column(Integer, ForeignKey(Contributor.id), nullable=False)
    UniqueConstraint("title", "course", "level", name="unique_handout")
