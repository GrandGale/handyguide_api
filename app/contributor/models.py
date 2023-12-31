from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKeyConstraint,
    Integer,
    String,
    DateTime,
    UniqueConstraint,
)

from app.config.database import DBBase


class Contributor(DBBase):
    __tablename__ = "contributors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String, nullable=False)
    university_id = Column(String(30), nullable=False)
    university = Column(String(10), nullable=False)
    level = Column(String(10), nullable=False)
    faculty = Column(Integer, nullable=False)
    department = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    is_contributor = Column(Boolean, default=True)
    is_supervisor = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    last_login = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now())

    ForeignKeyConstraint(
        ["university", "faculty", "department"],
        ["universities.abbrev", "faculties.id", "departments.id"],
    )
    UniqueConstraint(
        "university_id",
        "university",
        "level",
        "faculty",
        "department",
        name="unique_contributor",
    )
