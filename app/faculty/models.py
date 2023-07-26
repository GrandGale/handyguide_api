from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from ..university.models import University

from ..config.database import DBBase


class Faculty(DBBase):
    __tablename__ = "faculty"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    abbrev = Column(String(10), unique=True, index=True)
    university = Column(String, ForeignKey(University.abbrev))
    UniqueConstraint(name, university, name="unique_faculty")
