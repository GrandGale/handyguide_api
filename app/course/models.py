from sqlalchemy import Column, ForeignKey, String, Integer, UniqueConstraint

from app.department.models import Department
from app.faculty.models import Faculty
from app.level.models import Level
from app.university.models import University

from ..config.database import DBBase


class Course(DBBase):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(10), index=True, nullable=False)
    level = Column(String(10), ForeignKey(Level.abbrev), nullable=False)
    department = Column(String, ForeignKey(Department.abbrev), nullable=False)
    faculty = Column(String, ForeignKey(Faculty.abbrev), nullable=False)
    university = Column(String, ForeignKey(University.abbrev), nullable=False)
    UniqueConstraint(name, code, university, name="unique department")
