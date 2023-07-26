from fastapi import APIRouter

from app.config import database

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()
