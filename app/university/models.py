from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from ..config.database import DBBase


class University(DBBase):
    __tablename__ = "university"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True)
    abbrev = Column(String(10), unique=True, index=True)
    date_created = Column(DateTime, default=datetime.now())
