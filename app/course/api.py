from fastapi import APIRouter

from ..config import database

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()
