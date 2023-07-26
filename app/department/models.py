from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, Integer, UniqueConstraint
from app.faculty.models import Faculty

from app.university.models import University

from ..config.database import DBBase


class Department(DBBase):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    abbrev = Column(String(10), index=True)
    university = Column(String, ForeignKey(University.abbrev))
    faculty = Column(String, ForeignKey(Faculty.abbrev))
    UniqueConstraint(name, university, name="unique_department")
