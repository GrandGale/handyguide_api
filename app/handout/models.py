from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

from app.config.database import DBBase
from app.config.settings import settings
from app.course.models import Course
from app.department.models import Department
from app.faculty.models import Faculty
from app.university.models import University


class Handout(DBBase):
    __tablename__ = "handouts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), index=True)
    url = Column(String, default="/")
    upload_date = Column(DateTime, index=True, default=datetime.now())
    university = Column(String(10), ForeignKey(University.abbrev))
    faculty = Column(String(10), ForeignKey(Faculty.abbrev), nullable=True)
    department = Column(String(10), ForeignKey(Department.abbrev), nullable=True)
    course = Column(String(10), ForeignKey(Course.code))
    session = Column(String, default=settings.SESSION)
