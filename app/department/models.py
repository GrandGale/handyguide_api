from sqlalchemy import Column, ForeignKey, String, Integer, UniqueConstraint

from app.config.database import DBBase
from app.faculty.models import Faculty
from app.university.models import University


class Department(DBBase):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    abbrev = Column(String(10), index=True)
    faculty = Column(String, ForeignKey(Faculty.abbrev))
    university = Column(String, ForeignKey(University.abbrev))
    UniqueConstraint(name, university, abbrev, name="unique_department")
