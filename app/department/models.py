from sqlalchemy import Column, ForeignKey, String, Integer, UniqueConstraint

from app.config.database import DBBase
from app.faculty.models import Faculty
from app.university.models import University


class Department(DBBase):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    abbrev = Column(String(10), index=True, nullable=False)
    faculty = Column(String, ForeignKey(Faculty.abbrev), nullable=False)
    university = Column(String, ForeignKey(University.abbrev), nullable=False)
    UniqueConstraint(name, university, abbrev, name="unique_department")
