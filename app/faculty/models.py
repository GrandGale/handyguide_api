from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.config.database import DBBase
from app.university.models import University


class Faculty(DBBase):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    abbrev = Column(String(10), index=True)
    university = Column(String, ForeignKey(University.abbrev))
    UniqueConstraint(name, university, name="unique_faculty")
