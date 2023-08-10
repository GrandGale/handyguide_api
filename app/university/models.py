from datetime import datetime
from sqlalchemy import Column, String, DateTime

from app.config.database import DBBase


class University(DBBase):
    __tablename__ = "universities"

    name = Column(String(100), unique=True)
    abbrev = Column(String(10), primary_key=True, unique=True)
    date_created = Column(DateTime, default=datetime.now(), nullable=False)
