from sqlalchemy import Column, ForeignKey, String, Integer, UniqueConstraint

from app.department.models import Department
from app.faculty.models import Faculty
from app.university.models import University

from ..config.database import DBBase


class Course(DBBase):
    __tablename__ = "course"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100))
    code = Column(String(10), index=True)
    department = Column(String, ForeignKey(Department.abbrev))
    faculty = Column(String, ForeignKey(Faculty.abbrev))
    university = Column(String, ForeignKey(University.abbrev))
    UniqueConstraint(name, code, university, name="unique department")
