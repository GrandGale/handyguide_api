from sqlalchemy import Column, ForeignKey, String, Integer, UniqueConstraint

from app.department.models import Department
from app.faculty.models import Faculty
from app.level.models import Level
from app.university.models import University

from ..config.database import DBBase


class Course(DBBase):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    code = Column(String(10), index=True)
    level = Column(String(10), ForeignKey(Level.abbrev))
    department = Column(String, ForeignKey(Department.abbrev))
    faculty = Column(String, ForeignKey(Faculty.abbrev))
    university = Column(String, ForeignKey(University.abbrev))
    UniqueConstraint(name, code, university, name="unique department")
