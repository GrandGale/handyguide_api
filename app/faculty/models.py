from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.config.database import DBBase
from app.university.models import University


class Faculty(DBBase):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    abbrev = Column(String(10), index=True, nullable=False)
    university = Column(String, ForeignKey(University.abbrev), nullable=False)
    UniqueConstraint(name, university, name="unique_faculty")
