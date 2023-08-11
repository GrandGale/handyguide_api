from sqlalchemy import Column, String
from app.config.database import DBBase


class Level(DBBase):
    __tablename__ = "levels"

    name = Column(String(20), unique=True)
    abbrev = Column(String(10), primary_key=True)
